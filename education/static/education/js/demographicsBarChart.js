function drawChart(data, title) {

   //Set up SVG wtih proper margins
   var svgWidth = 500, svgHeight = 300;
   var margin = { top: 40, right: 20, bottom: 70, left: 50 };
   var width = svgWidth - margin.left - margin.right;
   var height = svgHeight - margin.top - margin.bottom;
   var svg = d3.select('svg')
     .attr("width", svgWidth)
     .attr("height", svgHeight);

   //Set up chart
   var chart = svg.append("g")
     .attr("transform",`translate(${margin.left}, ${margin.top})`);

   var x = d3.scaleBand()
     .domain(data.map((d) => d.group))
     .range([0, width])
     .padding(0.2);

   var y = d3.scaleLinear()
     .domain([0,100])
     .range([height, 0]);

   var insertLinebreaks = function (d) {
       var el = d3.select(this);
       var words = d.split('\n');
       el.text('');

       for (var i = 0; i < words.length; i++) {
           var tspan = el.append('tspan').text(words[i]);
           if (i > 0)
               tspan.attr('x', -2).attr('dy', '15');
       }
   };

   //add axes
   chart.append("g")
     .attr("transform", "translate(0," + height + ")")
     .call(d3.axisBottom(x).tickSize(0))
     .selectAll("text")
     .each(insertLinebreaks)
     .attr("dx", "-0.2em")
     .attr("dy", "0em")
     .style("text-anchor", "end")
     .attr("transform","rotate(-90)")
     .attr("white-space","pre");

   chart.append("g")
     .call(d3.axisLeft(y)
     .tickFormat(d3.format("d")));

   //add grid lines
   chart.append('g')
     .attr('class', 'graph-grid')
     .call(d3.axisLeft()
     .scale(y)
     .tickSize(-width, 0, 0)
     .tickFormat(''));

   //add data
   var tooltip = d3.select(".tooltip-label")
    .attr('class','tooltip-label');

   var bar = chart.selectAll()
      .data(data)
      .enter()
      .append('rect')
      .attr('class', 'graph-bar')
      .attr('id', (d) => d.group.split(' ')[0]+"-bar")
      .attr('x', (d) => x(d.group))
      .attr('y', (d) => y(d.value))
      .attr('height', (d) => height - y(d.value))
      .attr('width', x.bandwidth())
      .on('mouseenter', function (d) {
         tooltip.text(`Demographic: ${d.group}\nPercent: ${parseFloat(d.value).toFixed(1)}%`)
           .style("visibility", "visible")
           .style("left",(d3.event.pageX - 100) + "px")
           .style("top",(d3.event.pageY + 28) + "px")
      })
      .on('mouseleave', function () {
        tooltip.style("visibility", "hidden")
      });

   //add lables
   svg.append('text')
     .attr('class', 'graph-title')
     .attr('x', width / 2 + margin.left)
     .attr('y', margin.top/2)
     .text(`${title}`);

   svg.append('text')
     .attr('class', 'graph-label')
     .attr('x', -(height / 2) - margin.top)
     .attr('y', margin.left / 4)
     .attr('transform', 'rotate(-90)')
     .text('Percent of Cohort');
}
