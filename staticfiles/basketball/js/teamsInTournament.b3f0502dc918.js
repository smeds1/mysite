document.addEventListener("DOMContentLoaded", function() {
  drawChart(teams_in_tournament);
});

function drawChart(data) {

   //Set up SVG wtih proper margins
   var svgWidth = 600, svgHeight = 300;
   var margin = { top: 40, right: 20, bottom: 90, left: 50 };
   var width = svgWidth - margin.left - margin.right;
   var height = svgHeight - margin.top - margin.bottom;
   var svg = d3.select('svg')
     .attr("width", svgWidth)
     .attr("height", svgHeight);

   //Set up chart
   var chart = svg.append("g")
     .attr("transform",`translate(${margin.left}, ${margin.top})`);

   var x = d3.scaleBand()
     .domain(data.map((d) => d.conference))
     .range([0, width])
     .padding(0.2);

   var y = d3.scaleLinear()
     .domain([0,d3.max(data.map((d) => d.frequency))+1])
     .range([height, 0]);

   //add axes
   chart.append("g")
     .attr("transform", "translate(0," + height + ")")
     .call(d3.axisBottom(x).tickSize(0))
     .selectAll("text")
     .attr("dx", "-0.2em")
     .attr("dy", "0em")
     .style("text-anchor", "end")
     .attr("transform","rotate(-90)");

   chart.append("g")
     .call(d3.axisLeft(y)
     .tickFormat(d3.format("d")));

   //add grid lines
   chart.append('g')
     .attr('class', 'graph-grid')
     .call(d3.axisLeft()
     .scale(y)
     .tickSize(-width, 0, 0)
     .tickFormat(''))

   //add data
   var tooltip = d3.select("#teamsintournament_svg")
    .append("div")
    .attr('class','tooltip-label');

   var circle = chart.selectAll()
      .data(data)
      .enter()
      .append('rect')
      .attr('class', 'graph-bar')
      .attr('x', (d) => x(d.conference))
      .attr('y', (d) => y(d.frequency))
      .attr('height', (d) => height - y(d.frequency))
      .attr('width', x.bandwidth())
      .on('mouseenter', function (d) {

        var xPosition = parseFloat(d3.select(this).attr("x"))
				var yPosition = parseFloat(d3.select(this).attr("y")) - 40

        tooltip.text('Conference: '+ d.conference + '\nTeam Count: ' +d.frequency)
           .style("visibility", "visible")
           .style("left",parseFloat(xPosition) + "px")
           .style("top",parseFloat(yPosition) + "px")
      })
      .on('mouseleave', function () {
        tooltip.style("visibility", "hidden")
      })

   //add lables
   svg.append('text')
     .attr('class', 'graph-title')
     .attr('x', width / 2 + margin.left)
     .attr('y', margin.top/2)
     .text('Conferences Represented')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/8)
     .text('Conference')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 4)
     .attr('transform', 'rotate(-90)')
     .text('Count')
}
