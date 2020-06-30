let x_data = ['x']
let recovered_data = ['Recovered']
let confirmed_data = ['Confirmed']
let deaths_data = ['Deaths']


var top10_recovered_chart = c3.generate({
    bindto: '#bar1',
    data: {
        x: 'x',
        columns: [
            x_data.concat(top_ten_recovered['country']),
            recovered_data.concat(top_ten_recovered['recovered'])
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
            x_data.concat(top_ten_confirmed['country']),
            confirmed_data.concat(top_ten_confirmed['confirmed'])
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
            x_data.concat(top_ten_deaths['country']),
            deaths_data.concat(top_ten_deaths['deaths'])
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