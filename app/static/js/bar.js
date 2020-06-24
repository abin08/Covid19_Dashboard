var top10_recovered_chart = c3.generate({
    bindto: '#bar1',
    data: {
        x: 'x',
        columns: [
            ['x', 'USA', 'RUSSIA', 'UK', 'INDIA', 'UAE', 'AUS'],
            ['Recovered', 32, 190, 110, 390, 123, 21]
        ],
        type: 'bar'
    },
    axis: {
        x: {
            type: 'category'
        }
    },
    bar: {
        width: {
            ratio: 0.5
        }
    },
    color: {
        pattern: [RECOVERED_COLOR]
    },
    title: {
        text: 'Top Ten Recovered'
    }
});



var top10_active_chart = c3.generate({
    bindto: '#bar2',
    data: {
        x: 'x',
        columns: [
            ['x', 'USA', 'RUSSIA', 'UK', 'INDIA', 'UAE', 'AUS'],
            ['Active', 40, 220, 150, 300, 210, 180]
        ],
        type: 'bar'
    },
    axis: {
        x: {
            type: 'category'
        }
    },
    bar: {
        width: {
            ratio: 0.5
        }
    },
    color: {
        pattern: [ACTIVE_COLOR]
    },
    title: {
        text: 'Top Ten Confirmed'
    }
});


var top10_deaths_chart = c3.generate({
    bindto: '#bar3',
    data: {
        x: 'x',
        columns: [
            ['x', 'USA', 'RUSSIA', 'UK', 'INDIA', 'UAE', 'AUS'],
            ['Deaths', 299, 112, 167, 338, 189, 175]
        ],
        type: 'bar'
    },
    axis: {
        x: {
            type: 'category'
        }
    },
    bar: {
        width: {
            ratio: 0.5
        }
    },
    color: {
        pattern: [DEATHS_COLOR]
    },
    title: {
        text: 'Top Ten Deaths'
    }
});