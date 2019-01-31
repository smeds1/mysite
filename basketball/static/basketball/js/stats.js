document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("wp_by_elo_btn").onclick = () => {
    ajax_request("wp_by_elo",quantitativeBarChart,"ELO","Tournament Win Percentage",
      "Tournament Winning Percentage by ELO");
  }
  document.getElementById("wp_by_seed_btn").onclick = () => {
    ajax_request("wp_by_seed",qualitativeBarChart,"Seed","Tournament Win Percentage",
      "Tournament Winning Percentage by Seed");
  }
  document.getElementById("wp_by_conference_btn").onclick = () => {
    ajax_request("wp_by_conference",qualitativeBarChart,"Conference","Tournament Win Percentage",
      "Tournament Winning Percentage by Conference");
  }
  document.getElementById("wp_by_venue_capacity_btn").onclick = () => {
    ajax_request("wp_by_venue_capacity",quantitativeBarChart,"Home Venue Capacity",
      "Tournament Win Percentage","Tournament Winning Percentage by Home Venue Capacity");
  }
  document.getElementById("wp_by_ppg_btn").onclick = () => {
    ajax_request("wp_by_ppg",quantitativeBarChart,"In-Season PPG",
      "Tournament Win Percentage","Tournament Winning Percentage by Points Scored Per Game");
  }
  document.getElementById("wp_by_ppga_btn").onclick = () => {
    ajax_request("wp_by_ppga",quantitativeBarChart,"In-Season PPG Against",
      "Tournament Win Percentage","Tournament Winning Percentage by Points Per Game Against");
  }
  document.getElementById("wp_by_ppgd_btn").onclick = () => {
    ajax_request("wp_by_ppgd",quantitativeBarChart,"In-Season PPG Differential",
      "Tournament Win Percentage","Tournament Winning Percentage by Points Per Game Differential");
  }
  document.getElementById("matchup_by_elo_btn").onclick = () => {
    ajax_request("matchup_by_elo",quantitativeBarChart,"Difference in ELOs",
      "Lower ELO Team Win %","Percent of Time Lower ELO Team Wins in Tournament Game");
  }
  document.getElementById("matchup_by_seed_btn").onclick = () => {
    ajax_request("matchup_by_seed",qualitativeBarChart,"Difference in Seeds",
      "Lower Seed Win %","Percent of Time Lower Seed Wins in Tournament Game");
  }
  document.getElementById("matchup_by_ppg_btn").onclick = () => {
    ajax_request("matchup_by_ppg",quantitativeBarChart,"Difference in PPG",
      "Lower PPG Team Win %","Percent of Time Lower PPG Team Wins in Tournament Game");
  }
  document.getElementById("wp_by_elo_btn").click();
});

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajax_request(graph,f,x_var,y_var,title){
  $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
             xhr.setRequestHeader("X-CSRFToken", csrftoken);
         }
     }
  });
  $.ajax({
    type: "POST",
    url: '/basketball/ajax/stats_graph/',
    data: {'graph': graph},
    dataType: 'json',
    success: function (data) {
      f(JSON.parse(data['wp']),x_var,y_var,title);
      //console.log(data['wp']);
    }
  });
}

function quantitativeBarChart(data,x_var,y_var,title) {

   $("svg").empty();

   //Set up SVG wtih proper margins
   var svgWidth = 500, svgHeight = 300;
   var margin = { top: 40, right: 20, bottom: 40, left: 50 };
   var width = svgWidth - margin.left - margin.right;
   var height = svgHeight - margin.top - margin.bottom;
   var svg = d3.select('svg')
     .attr("width", svgWidth)
     .attr("height", svgHeight);
   const min_bin = parseInt(data[0].bin);
   const max_bin = parseInt(data[data.length-1].bin);
   var bin_width = max_bin;
   for(var i=1; i<data.length; i++){
     if(data[i].bin - data[i-1].bin < bin_width){
       bin_width = data[i].bin - data[i-1].bin;
     }
   }

   if (max_bin > 10000){
     format = d3.format(",.0f");
   }
   else{
     format = d3.format("d");
   }

   //Set up chart
   var chart = svg.append('g')
      .attr('transform',`translate(${margin.left}, ${margin.top})`)

   var xScale = d3.scaleLinear()
     .domain([min_bin, max_bin + bin_width])
     .range([0, width]);

   var yScale = d3.scaleLinear()
       .range([height, 0])
       .domain([0, 100]);

   //add axes
   chart.append('g')
       .attr('transform', `translate(0, ${height})`)
       .call(d3.axisBottom(xScale)
          .tickValues(d3.range(min_bin, max_bin+2*bin_width, bin_width))
          .tickFormat(format))
       .selectAll("text")
       .style("text-anchor", "middle");

   chart.append('g')
      .call(d3.axisLeft(yScale)
          .tickFormat(d => d + "%"));

   //add grid lines
   chart.append('g')
       .attr('class', 'graph-grid')
       .call(d3.axisLeft()
       .scale(yScale)
       .tickSize(-width, 0, 0)
       .tickFormat(''))

   //add data
   var tooltip = d3.select(".tooltip-label")
    .attr('class','tooltip-label');

   var bar = chart.selectAll()
    .data(data)
    .enter()
    .append('rect')
    .attr('class', 'graph-bar')
    .attr('x', (d) => xScale(d.bin)+0.5)
    .attr('y', (d) => yScale(d.wp))
    .attr('height', (d) => height - yScale(d.wp))
    .attr('width', xScale(bin_width+min_bin)-0.5)
    .on('mouseenter', function (d) {

      tooltip.text(`${x_var}: ${format(d.bin)} - ${format(Number(d.bin)+bin_width)}\n${y_var}: ${parseFloat(d.wp).toFixed(1)}%`)
         .style("visibility", "visible")
         .style("left",(d3.event.pageX - 100) + "px")
         .style("top",(d3.event.pageY - 60) + "px")
    })
    .on('mouseleave', function () {
      tooltip.style("visibility", "hidden")
    })

   //add lables
   svg.append('text')
     .attr('class', 'graph-title')
     .attr('x', width / 2 + margin.left)
     .attr('y', margin.top/2)
     .text(title)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text(x_var)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 4)
     .attr('transform', 'rotate(-90)')
     .text(y_var)
}

function qualitativeBarChart(data,x_var,y_var,title) {
   $("svg").empty();

   //Set up SVG wtih proper margins
   var svgWidth = 500, svgHeight = 300;
   if (data[0].value.length > 2){
     var margin = { top: 40, right: 20, bottom: 90, left: 50 };
   }
   else{
     var margin = { top: 40, right: 20, bottom: 40, left: 50 };
   }
   var width = svgWidth - margin.left - margin.right;
   var height = svgHeight - margin.top - margin.bottom;
   var svg = d3.select('svg')
     .attr("width", svgWidth)
     .attr("height", svgHeight);

   //Set up chart
   var chart = svg.append('g')
      .attr('transform',`translate(${margin.left}, ${margin.top})`)

   var xScale = d3.scaleBand()
       .range([0, width])
       .domain(data.map((d) => d.value))
       .padding(0.01)

   var yScale = d3.scaleLinear()
       .range([height, 0])
       .domain([0, 100]);

   //add axes
   var xaxis = chart.append('g')
       .attr('transform', `translate(0, ${height})`)
       .call(d3.axisBottom(xScale).tickSize(0))
       .selectAll("text");

  if (data[0].value.length > 2){ //tilt long category names
    xaxis.attr("dx", "-0.2em")
    .attr("dy", "0em")
    .style("text-anchor", "end")
    .attr("transform","rotate(-90)");
  }

   chart.append('g')
      .call(d3.axisLeft(yScale)
        .tickFormat(d => d + "%"));

   //add grid lines
   chart.append('g')
       .attr('class', 'graph-grid')
       .call(d3.axisLeft()
       .scale(yScale)
       .tickSize(-width, 0, 0)
       .tickFormat(''))

   //add data
   var tooltip = d3.select(".tooltip-label")
    .attr('class','tooltip-label');

   var bar = chart.selectAll()
    .data(data)
    .enter()
    .append('rect')
    .attr('class', 'graph-bar')
    .attr('x', (d) => xScale(d.value))
    .attr('y', (d) => yScale(d.wp))
    .attr('height', (d) => height - yScale(d.wp))
    .attr('width', xScale.bandwidth())
    .on('mouseenter', function (d) {

      tooltip.text(`${x_var}: ${d.value}\n${y_var}: ${parseFloat(d.wp).toFixed(1)}%`)
         .style("visibility", "visible")
         .style("left",(d3.event.pageX - 100) + "px")
         .style("top",(d3.event.pageY - 60) + "px")
    })
    .on('mouseleave', function () {
      tooltip.style("visibility", "hidden")
    })

   //add lables
   svg.append('text')
     .attr('class', 'graph-title')
     .attr('x', width / 2 + margin.left)
     .attr('y', margin.top/2)
     .text(title)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text(x_var)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 4)
     .attr('transform', 'rotate(-90)')
     .text(y_var)
}
