document.addEventListener("DOMContentLoaded", function() {
     drawChart(elo_by_year);
});

function drawChart(data) {

   //Set up SVG wtih proper margins
   var svgWidth = 450, svgHeight = 250;
   var margin = { top: 40, right: 30, bottom: 60, left: 60 };
   var width = svgWidth - margin.left - margin.right;
   var height = svgHeight - margin.top - margin.bottom;
   var svg = d3.select('svg')
     .attr("width", svgWidth)
     .attr("height", svgHeight);

   //Set up chart
   var chart = svg.append("g")
     .attr("transform",`translate(${margin.left}, ${margin.top})`);

   var x = d3.scaleLinear()
     .domain(d3.extent(data, function(d) { return d.year; }))
     .range([0, width]);
   var y = d3.scaleLinear()
     .domain([d3.min(data, function(d) {return d.elo;})-20, d3.max(data, function(d) {return d.elo;})+20])
     .range([height, 0]);

   var line = d3.line()
     .x(function(d) { return x(d.year); })
     .y(function(d) { return y(d.elo); });

   //add axes
   chart.append("g")
     .attr("transform", "translate(0," + height + ")")
     .call(d3.axisBottom(x).tickFormat(d3.format("d")));

   chart.append("g")
     .call(d3.axisLeft(y).tickFormat(d3.format("d")));

   //add grid lines
   chart.append('g')
     .attr('class', 'graph-grid')
     .call(d3.axisLeft()
     .scale(y)
     .tickSize(-width, 0, 0)
     .tickFormat(''))

   //add data
   chart.append("path")
     .attr('class','graph-line')
     .data([data])
     .attr("d", line);

   //add circles
   var tooltip = d3.select("#elo_svg")
    .append("div")
    .attr('class','tooltip-label');

   var circle = chart.selectAll()
      .data(data)
      .enter()
      .append('circle')
      .attr('class', 'graph-circle')
      .attr('cx', (d) => x(d.year))
      .attr('cy', (d) => y(d.elo))
      .on('mouseenter', function (d) {

        var xPosition = parseFloat(d3.select(this).attr("cx")) + 40
				var yPosition = parseFloat(d3.select(this).attr("cy")) - 40

        tooltip.html(`<table><tr><td>Year:</td><td>${d.year}</td></tr><tr><td>ELO:</td><td>${d.elo}</td></tr></table>`)
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
     .text('ELO Rating over Time')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', width / 2 + margin.left)
     .attr('y', svgHeight - margin.bottom/3)
     .text('Year')

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 3)
     .attr('transform', 'rotate(-90)')
     .text('ELO Rating')
}
