import React, { useEffect, useState } from 'react';

function CountriesList() {
    const [countries, setCountries] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/countries-and-capitals')
            .then(response => response.json())
            .then(data => setCountries(data));
    }, []);

    return (
        <div>
            <h1>Countries and Capitals</h1>
            <ul>
                {countries.map((item, index) => (
                    <li key={index}>
                        {item.country} - {item.capital}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default CountriesList;
