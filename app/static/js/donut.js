var chart1 = c3.generate({
    bindto: '#donut',
    data: {
        columns: [
            ['Active', total_covid_info['total_active']],
            ['Recovered',  total_covid_info['total_recovered']],
            ['Deaths',  total_covid_info['total_deaths']]
        ],
        type : 'donut',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    donut: {
        title: "Total Cases: " + numberWithCommas(total_covid_info['total_confirmed'])
    },
    color: {
        pattern: [ACTIVE_COLOR, RECOVERED_COLOR, DEATHS_COLOR]
    }
});

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}