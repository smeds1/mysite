document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("wp_by_elo_btn").onclick = () => {
    ajax_request("wp_by_elo",quantitativeBarChart,"ELO");
  }
  document.getElementById("wp_by_seed_btn").onclick = () => {
    ajax_request("wp_by_seed",drawChart2,null);
  }
  document.getElementById("wp_by_conference_btn").onclick = () => {
    ajax_request("wp_by_conference",drawChart3,null);
  }
  document.getElementById("wp_by_venue_capacity_btn").onclick = () => {
    ajax_request("wp_by_venue_capacity",quantitativeBarChart,"Home Venue Capacity");
  }
  document.getElementById("wp_by_ppg_btn").onclick = () => {
    ajax_request("wp_by_ppg",quantitativeBarChart,"Regular Season PPG");
  }
  document.getElementById("wp_by_elo_btn").click();
});

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajax_request(graph,f,variable){
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
      if(f.name == "quantitativeBarChart"){
        f(JSON.parse(data['wp']),variable);
      }
      else{
        f(JSON.parse(data['wp']));
      }

    }
  });
}

function drawChart2(data) {
   $("svg").empty();

   //Set up SVG wtih proper margins
   var svgWidth = 500, svgHeight = 300;
   var margin = { top: 40, right: 20, bottom: 40, left: 50 };
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
       .domain(data.map((d) => d.tournament_seed))
       .padding(0.01)

   var yScale = d3.scaleLinear()
       .range([height, 0])
       .domain([0, 100]);

   //add axes
   chart.append('g')
       .attr('transform', `translate(0, ${height})`)
       .call(d3.axisBottom(xScale))
       .selectAll("text")
       .style("text-anchor", "middle");

   chart.append('g')
      .call(d3.axisLeft(yScale));

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
    .attr('x', (d) => xScale(d.tournament_seed))
    .attr('y', (d) => yScale(d.wp))
    .attr('height', (d) => height - yScale(d.wp))
    .attr('width', xScale.bandwidth())
    .on('mouseenter', function (d) {

      tooltip.text(`Seed: ${d.tournament_seed}\nWin Percentage: ${parseFloat(d.wp).toFixed(1)}%`)
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
     .text('Tournament Winning Percentage by Seed')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text('Seed')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 2.5)
     .attr('transform', 'rotate(-90)')
     .text('Percent of Games Won')
}

function drawChart3(data) {
   $("svg").empty();

   //Set up SVG wtih proper margins
   var svgWidth = 500, svgHeight = 300;
   var margin = { top: 40, right: 20, bottom: 90, left: 50 };
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
       .domain(data.map((d) => d.conference) )
       .padding(0.01)

   var yScale = d3.scaleLinear()
       .range([height, 0])
       .domain([0, 100]);

   //add axes
   chart.append('g')
       .attr('transform', `translate(0, ${height})`)
       .call(d3.axisBottom(xScale).tickSize(0))
       .selectAll("text")
       .attr("dx", "-0.2em")
       .attr("dy", "0em")
       .style("text-anchor", "end")
       .attr("transform","rotate(-90)");

   chart.append('g')
      .call(d3.axisLeft(yScale));

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
    .attr('x', (d) => xScale(d.conference))
    .attr('y', (d) => yScale(d.wp))
    .attr('height', (d) => height - yScale(d.wp))
    .attr('width', xScale.bandwidth())
    .on('mouseenter', function (d) {

      tooltip.text(`Conference: ${d.conference}\nWin Percentage: ${parseFloat(d.wp).toFixed(1)}%`)
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
     .text('Tournament Winning Percentage by Conference')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text('Conference')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 2.5)
     .attr('transform', 'rotate(-90)')
     .text('Percent of Games Won')
}

function quantitativeBarChart(data,variable) {

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
     .domain([Math.max(0,min_bin), max_bin + bin_width])
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
      .call(d3.axisLeft(yScale));

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

      tooltip.text(`${variable}: ${format(d.bin)} - ${format(Number(d.bin)+bin_width)}\nWin Percentage: ${parseFloat(d.wp).toFixed(1)}%`)
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
     .text(`Tournament Winning Percentage by ${variable}`)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text(`${variable}`)

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 2.5)
     .attr('transform', 'rotate(-90)')
     .text('Percent of Games Won')
}
