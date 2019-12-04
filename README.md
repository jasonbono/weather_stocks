# weather_stocks


Weather affects people's mood. Does it systematically and measurably affect the behavior of wall-street investors?

This is an exploratory analysis that looks for correlations between stock motion and changes in the weather. It is intended as a slow burn project, starting with simple analyses that grow in complexity over time.



**Preliminary Choices:** Localize to NYC

To start, the Dow Jones Industrial Average (DJIA) was used because its a major market index that, to some extent, captures the expectations of earnings and risk of investors located in NYC, and so may plausibly have some sensitivity to local conditions. 

Ideally, the global distribution of investors affecting the DJIA should be used to weight global weather conditions. However, to start, we use the weather as reported in the Central Park weather station.

## Getting Started
These instructions will help get you a copy of the project up and running on your local machine.

### Prerequisites
- python 3
- numpy (tested on version 1.17.0)
- pandas (tested on version 0.25.0)

## Contributing

1. Fork it (<https://github.com/jasonbono/MuonConvolution/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


## Authors

* **Jason Bono** - *Initial work* - [JasonBono](https://github.com/JasonBono)


## Acknowledgments

* Thank you to NOAA for providing the weather data

