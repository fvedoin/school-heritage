Highcharts.getSVG = function (charts, options, callback) {
    var svgArr = [],
        top = 0,
        width = 0,
        addSVG = function (svgres) {
            // Grab width/height from exported chart
            var svgWidth = +svgres.match(
                /^<svg[^>]*width\s*=\s*\"?(\d+)\"?[^>]*>/
                )[1],
                svgHeight = +svgres.match(
                    /^<svg[^>]*height\s*=\s*\"?(\d+)\"?[^>]*>/
                )[1],
                // Offset the position of this chart in the final SVG
                svg = svgres.replace('<svg', '<g transform="translate(0,' + top + ')" ');
            svg = svg.replace('</svg>', '</g>');
            top += svgHeight;
            width = Math.max(width, svgWidth);
            svgArr.push(svg);
        },
        exportChart = function (i) {
            if (i === charts.length) {
                return callback('<svg height="' + top + '" width="' + width +
                    '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + svgArr.join('') + '</svg>');
            }
            charts[i].getSVGForLocalExport(options, {}, function () {
                console.log("Failed to get SVG");
            }, function (svg) {
                addSVG(svg);
                return exportChart(i + 1); // Export next only when this SVG is received
            });
        };
    exportChart(0);
};

/**
 * Create a global exportCharts method that takes an array of charts as an argument,
 * and exporting options as the second argument
 */
Highcharts.exportCharts = function (charts, options) {
    options = Highcharts.merge(Highcharts.getOptions().exporting, options);
    // Get SVG asynchronously and then download the resulting SVG
    Highcharts.getSVG(charts, options, function (svg) {
        Highcharts.downloadSVGLocal(svg, options, function () {
            console.log("Failed to export on client side");
        });
    });
};

// Set global default options for all charts
Highcharts.setOptions({
    exporting: {
        fallbackToExportServer: false // Ensure the export happens on the client side or not at all
    }
});

var gaugeOptions = {
    chart: {
        type: 'solidgauge',
        marginTop: 60
    },
    pane: {
        center: ['50%', '85%'],
        size: '140%',
        startAngle: -90,
        endAngle: 90,
        background: {
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#EEE',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc'
        }
    },

    exporting: {
        enabled: false
    },

    tooltip: {
        enabled: false
    },

    // the value axis
    yAxis: {
        stops: [
            [0.1, '#55BF3B'], // green
            [0.5, '#DDDF0D'], // yellow
            [0.9, '#DF5353'] // red
        ],
        lineWidth: 0,
        tickWidth: 0,
        minorTickInterval: null,
        tickAmount: 2,
        title: {
            y: -70
        },
        labels: {
            y: 16
        }
    },

    plotOptions: {
        solidgauge: {
            dataLabels: {
                y: 5,
                borderWidth: 0,
                useHTML: true
            }
        }
    }
};

function displayGraph(id, value, max, title, spanText, valueSuffix) {
    Highcharts.chart(id, Highcharts.merge(gaugeOptions, {
        title: {
            text: title
        },

        yAxis: {
            min: 0,
            max: max,
            tickPositioner: function () {
                var tickPositions = this.tickPositions,
                    lastTick = tickPositions[tickPositions.length - 1],
                    max = this.options.max;

                if (lastTick > max) {
                    tickPositions.pop(); // remove last tick
                    tickPositions.push(max);
                }
            }
        },

        credits: {
            enabled: false
        },

        series: [{
            name: title,
            data: [value],
            dataLabels: {
                format:
                    '<div style="text-align:center">' +
                    '<span style="font-size:25px">{y}</span><br/>' +
                    '<span style="font-size:12px;opacity:0.4">' + spanText + '</span>' +
                    '</div>'
            },
            tooltip: {
                valueSuffix: valueSuffix
            }
        }]

    }));
}

$(".data").mask("00/00/0000");
$('.data').datepicker({
    dateFormat: 'dd/mm/yy',
    dayNames: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
    dayNamesMin: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S', 'D'],
    dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
    monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    nextText: 'Próximo',
    prevText: 'Anterior',
    maxDate: '0'
});

$('#createProblemsDateIni').change(function () {
    searchProblemsCreated();
});

$('#createProblemsDateFin').change(function () {
    searchProblemsCreated();
});

function searchProblemsCreated() {
    const initial_date = $('#createProblemsDateIni').val();
    const final_date = $('#createProblemsDateFin').val()
    $.ajax({
        url: "/relatorio/buscar-problemas-criados",
        type: 'get',
        data: {
            initial_date: initial_date,
            final_date: final_date
        },
        datatype: 'json'
    }).done(function (json) {
        $('#errorGraphProblemsCreated').html('');
        if (json.success) {
            charts = Highcharts.charts;
            charts.forEach(function (chart, index) {
                if (chart.renderTo.id === 'container-problems-created') {
                    chart.title.update({
                        text: 'Problemas criados <br>entre ' + initial_date + ' e ' + final_date
                    })
                    chosenChart = chart;
                    var point = chart.series[0].points[0]
                    point.update(json.message)
                }
            });
        } else {
            $('#errorGraphProblemsCreated').html(json.message)
        }
    });
}

$('#resolvedProblemsDateIni').change(function () {
    searchProblemsResolved();
});

$('#resolvedProblemsDateFin').change(function () {
    searchProblemsResolved();
});

function searchProblemsResolved() {
    const initial_date = $('#resolvedProblemsDateIni').val();
    const final_date = $('#resolvedProblemsDateFin').val()
    $.ajax({
        url: "/relatorio/buscar-problemas-resolvidos",
        type: 'get',
        data: {
            initial_date: initial_date,
            final_date: final_date
        },
        datatype: 'json'
    }).done(function (json) {
        $('#errorGraphProblemsResolved').html('');
        if (json.success) {
            charts = Highcharts.charts;
            charts.forEach(function (chart, index) {
                if (chart.renderTo.id === 'container-problems-resolved') {
                    chart.title.update({
                        text: 'Problemas resolvidos <br>entre ' + initial_date + ' e ' + final_date
                    })
                    chosenChart = chart;
                    var point = chart.series[0].points[0]
                    point.update(json.message)
                }
            });
        } else {
            $('#errorGraphProblemsResolved').html(json.message)
        }
    });
}

$('#export').click(function () {
    Highcharts.exportCharts(Highcharts.charts, {
        type: 'application/pdf',
        filename: 'relatorio-patrimonio'
    });
});