$( document ).ready(function() {

  $.getJSON('http://localhost:8080/data.json', function (response) {
    for (var i = 0, len = response.length; i < len; i++) {
      // create DOM

      $("#container").append("<div id='" + response[i].id + "' style='height: 900px; min-width: 310px'>");
      t = processSignals(response[i].signal)
      evaluate(response[i].ohlc, t)
      createOHLC(response[i].id, response[i].name, response[i].ohlc, response[i].close, response[i].ac, t)
    }
  })

})


function createOHLC(id, title, ohlc, close, ac, ss) {

   // create the chart
   var chart = Highcharts.stockChart(id, {
     chart: {
       margin: 0
     },

     boost: {
        useGPUTranslations: true
      },

     title: {
       text: title
     },

     yAxis: [{
      labels: {
        align: 'right',
        x: -3
      },
      title: {
        text: 'OHLC'
      },
      height: '70%',
      lineWidth: 0.2
    }, {
      labels: {
        align: 'right',
        x: -3
      },
      title: {
        text: 'Accelerator Oscillator'
      },
      top: '70%',
      height: '30%',
      offset: 0,
    }],


    series: [{
        type: 'candlestick',
        name: id,
        id: id,
        data: ohlc
      },
      {
        type: 'line',
        name: 'Close',
        data: close,
        color: "#666"
      },
      {
        type: 'column',
        name: 'AC',
        data: ac,
        yAxis: 1,
        color: "#bae1ff"
      },
      {
       type: 'flags',
       name: 'Signals',
       data: ss,
       yAxis: 0,
       shape: 'squarepin'
      }

    ],

     scrollbar: {
       enabled: true
     },

     rangeSelector: {
       enabled: true
     },

     navigator: {
       enabled: true
     },

     tooltip: {
       enabled: true
     }

   })
 }

function processSignals(data) {

  var signal = []
  var s;
  for (var i = 0, len = data.length; i < len; i++) {
    if(data[i][1] == 1) {
      s = "Buy"
    } else if (data[i][1] == -1) {
      s = "Sell"
    }

    signal.push({
      x: data[i][0], // the date
      title: s,
      text: s
    })

  }

  return signal
}


 // EMA for closing prices
 function ema(data, days) {
   // variables for EMA
   var k = 2 / (days + 1)
   var emaToday = 0
   var emaYesterday = 0

   var ema = []
   for (var i = 0, len = data.length; i < len; i++) {
     // calculate EMA(20)
      if (i >= days) {
        emaYesterday = (emaYesterday == null) ? 0 : emaYesterday
        emaToday = data[i][4] * k + (emaYesterday * (1 - k))
      } else {
        emaToday = null
      }

      if(emaToday) {
        ema.push([
          data[i][0], // the date
          emaToday
        ])
      }

      emaYesterday = emaToday // set to today's ema
   }
   return ema
 }

 // series1 should be the long
 function crossover(seriesLong, seriesShort, seriesOffsetLong, seriesOffsetShort) {
   var cs = []
   var offsetDiff = seriesOffsetLong - seriesOffsetShort
   for (var i = 1, len = seriesLong.length; i < len; i++) {
         if(seriesShort[offsetDiff + i][1] > seriesLong[i][1] &&
         seriesShort[offsetDiff + i - 1][1] < seriesLong[i - 1][1]) {
           cs.push({
             x: seriesLong[i][0], // the date
             title: "Buy"
           })
         }

         if(seriesShort[offsetDiff + i][1] < seriesLong[i][1] &&
         seriesShort[offsetDiff + i - 1][1] > seriesLong[i - 1][1]) {
           cs.push({
             x: seriesLong[i][0], // the date
             title: "Sell"
           })
         }
   }

   return cs
 }


 function evaluate(series, triggers) {
   var startCash = 10000
   var currentCash = startCash
   var holdingPosition = false
   var sellCommission = (0.795/100)
   var buyCommission = (0.295/100)
   var buyAdjustedPrice = 0
   var sellAdjustedPrice = 0
   var profitFromTrade = 0
   var totalProfitFromTrades = 0
   var numOfTrades = 0
   console.log(t);
   for (var i = 0, len = series.length; i < len; i++) {
       for (var j = 0, lenj = triggers.length; j < lenj; j++) {
         if(series[i][0] == triggers[j].x){
           if(triggers[j].title === "Buy" && !holdingPosition && i < series.length - 1) {
             buyAdjustedPrice = series[i+1][1] + (series[i+1][1] * buyCommission)
             holdingPosition = true
             // console.log("Date: " + series[i][0]);
             // console.log("Buy: " + buyAdjustedPrice);
           }
           if(triggers[j].title === "Sell" && holdingPosition && i < series.length - 1) {
             sellAdjustedPrice = series[i+1][1] - (series[i+1][1] * sellCommission)
             holdingPosition = false
             profitFromTrade = sellAdjustedPrice - buyAdjustedPrice
             currentCash = currentCash + profitFromTrade
             totalProfitFromTrades = totalProfitFromTrades + profitFromTrade
             numOfTrades += 1
             // console.log("Date: " + new Date(series[i][0]).toString());
             // console.log("Sell: " + sellAdjustedPrice);
             // console.log("Profit: " + profitFromTrade);
           }
         }
       }
   }

   console.log("Overall Profit: " + (currentCash - startCash));
   console.log("Number of Trades: " + numOfTrades);
   console.log("Average Profit per Trade: " + (totalProfitFromTrades/numOfTrades));
   console.log("Growth: " + (((currentCash - startCash) / startCash) * 100));

 }
