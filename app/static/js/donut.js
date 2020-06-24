var chart1 = c3.generate({
    bindto: '#donut',
    data: {
        columns: [
            ['Total Active', total_covid_info['total_active']],
            ['Total Recovered',  total_covid_info['total_recovered']],
            ['Total Deaths',  total_covid_info['total_deaths']],
        ],
        type : 'donut',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    },
    donut: {
        title: "Global Status"
    },
    color: {
        pattern: [ACTIVE_COLOR, RECOVERED_COLOR, DEATHS_COLOR]
    }
});
