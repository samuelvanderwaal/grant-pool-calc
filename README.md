# Factom Grant Pool Future Size Calculator

This is a simple utility tool for calculating the size of the Factom community grant pool at future dates. 

## Usage
To use it, simply pass as a command line argument the desired date at which to calculate the grant pool size. The tool accepts most date and time formats but assumes UTC timezone. 

E.g. `python grant-pool-calculator.py "2019-03-01 00:00"` or
`python grant-pool-calculator.py 2019-02-27T12:00`.

## Limitations
Forecasting into the future past an unpaid grant round will yield inaccurate results. The calculation should be rerun if any ANOs change their efficiencies or there are additions or subtractions to the authority set.