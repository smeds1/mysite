document.addEventListener("DOMContentLoaded", function() {
  drawMap(population_data,popsvg,`Percent of Population that is ${group}`);
  drawMap(rate_data,ratesvg,`${group} Graduation Rate`);
});
