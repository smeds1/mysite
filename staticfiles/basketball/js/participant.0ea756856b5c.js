document.addEventListener("DOMContentLoaded", function() {
     drawPieChart(finish_data);
});

function drawPieChart(data){

  //Set up SVG wtih proper margins
  var svgWidth = 300, svgHeight = 300;
  var margin = { top: 40, right: 40, bottom: 40, left: 40 };
  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;
  var svg = d3.select('#finishes_svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .attr("text-anchor", "middle");

  //Set up chart
  var chart = svg.append('g')
     .attr('transform',`translate(${width/2+margin.left}, ${height/2+margin.top})`)

  var pie = d3.pie()
    .sort(null)
    .value(d => d.value)

  var arc = d3.arc()
    .innerRadius(0)
    .outerRadius(Math.min(width/2, height/2) - 1)

  var color = d3.scaleOrdinal()
     .domain(data.map(d => d.place))
     .range(['#c6dbef','#4292c6','#084594']);

  //put data on graph
  chart.selectAll("path")
    .data(pie(data))
    .enter()
    .append("path")
    .attr("fill", d => color(d.data.place))
    .attr("stroke", "white")
    .attr("d", arc);

  //put labels on  graph
  var arcLabel = d3.arc()
    .innerRadius(Math.min(width/2, height/2) * 0.6)
    .outerRadius(Math.min(width/2, height/2) * 0.6);

  const text = chart.selectAll("text")
    .data(pie(data))
    .enter()
    .append("text")
    .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
    .attr("dy", "0.35em");

  text.append("tspan")
    .attr("x", 0)
    .attr("y", "-0.7em")
    .text(d => `${d.data.place} Place`);

  text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
    .attr("x", 0)
    .attr("y", "0.7em")
    .attr("fill-opacity", 0.7)
    .text(d => `(${d.data.value.toLocaleString()} times)`);

  //add title
  svg.append('text')
    .attr('class', 'graph-title')
    .attr('x', width / 2 + margin.left)
    .attr('y', margin.top/2)
    .text('Tournament Placement Since 2006')
}
