function changeAnimEase(element){
    console.log(element);
    animEase = element.value;
    drawChart();
}

function changeAnimDuration(element){
    animDuration = element.value;
    drawChart();
}

function changeChartTheme(element){
    chartTheme = element.value;
    drawChart();
}

function changeReversalType(element){
    reversalType = element.value;
    drawChart();
}

function changeReversalValue(){
    reversalValue = element.value;
    drawChart();
}

function showBreakPoints(element){
    breakPoints = element.checked;
    drawChart();
}

function showLegend(element){
    legend = element.checked;
    drawChart();
}

function showBreakPointTooltip(element){
    breakPointTooltips = element.checked;
    drawChart();
}

function showBreakPoints(element){
    breakPoints = element.checked;
    drawChart();
}

function showBreakPointText(element){
    breakPointText = element.checked;
    drawChart();
}

function showAnimation(element){
    animation = element.checked;
    drawChart();
}

function showRangePointTooltips(element){
    rangeTooltips = element.checked;
    drawChart();
}

function changeCaption(element){
    caption = element.value;
    drawChart();
}

function changeSubCaption(element){
    subCaption = element.value;
    drawChart();
}

function changeRallyColor(element){
    rallyColor = element.value;
    drawChart();
}

function changeRallyThickness(element){
    rallyThickness = element.value;
    drawChart();
}

function changeRallyThicknessOnHover(element){
    rallyThicknessOnHover = element.value;
    drawChart();
}

function changeDeclineColor(element){
    declineColor = element.value;
    drawChart();
}

function changeDeclineThickness(element){
    declineThickness = element.value;
    drawChart();
}

function changeDeclineThicknessOnHover(element){
    declineThicknessOnHover = element.value;
    drawChart();
}

function changeBreakPointRadius(element){
    breakPointRadius = element.value;
    drawChart();
}

function changeBreakPointRadiusOnHover(element){
    breakPointRadiusOnHover = element.value;
    drawChart();
}

function changeBreakPointColor(element){
    breakPointColor = element.value;
    drawChart();
}

function drawChart(){
    var chartElement = document.getElementById("kagiChart");
    chartElement.innerHTML="";

    var chart_options = {
      "caption": "Caption",
      "subCaption": "Sub caption",
      "reversalValue": 2,
      "reversalType": "diff",
      "unit": "$",
      "isPrecedingUnit":true,
      "rallyThickness": "2",
      "rallyThicknessOnHover": "3",
      "declineThickness": "2",
      "declineThicknessOnHover": "3",
      "rallyColor": "#43942e",
      "declineColor": "#f13558",
      "width":900,
      "height":500,
      "margin":{top: 75, right: 50, bottom: 100, left: 50},
      "showBreakPoints":true,
      "showBreakPointText":true,
      "breakPointColor":"#1c2232",
      "breakPointRadius":3,
      "breakPointRadiusOnHover":7,
      "showBreakPointTooltips":true,
      "showRangeTooltips":true,
      "showLegend":true,
      "chartTheme":"light",
      "showAnimation":false,
      "animationDurationPerTrend":100,
      "animationEase":"linear"
    }

    KagiChart(data,chart_options); // data is served from data.js
}
drawChart();
