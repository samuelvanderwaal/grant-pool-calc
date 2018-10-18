# Factom Grant Pool Future Size Calculator

This is a simple utility tool for calculating the size of the Factom community grant pool at some date in the future. To use you need to get the size of the grant pool currently from [Factoshi.io](https://factoshi.io/price_and_supply) and the daily amount contributed to the pool from the [TFA Explorer](https://explorer.factoid.org/) or [Luciap's tool](https://luciap.ca/#/authority-set). 

Pass these values as arguments to the tool in addition to the ending date you want to calculate the size of the grant pool at. The tool accepts most date and time formats but assumes UTC timezone. 

E.g. `python grant-pool-calculator.py 96412.37 1396.41 "2018-11-14 00:00"` or
`python grant-pool-calculator.py 104302.91 1401.27 2018-11-17T12:00`.
