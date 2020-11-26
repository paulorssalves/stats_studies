
miles_traveled = c(89, 66, 78, 111, 44, 77, 80, 66, 109, 76)
num_deliveries = c(4, 1, 3, 6, 1, 3, 3, 2, 5, 3)
gas_price = c(3.84, 3.19, 3.78, 3.89, 3.57, 3.57, 3.03,3.51, 3.45, 3.25)
travel_time = c(7, 5.4, 6.6, 7.4, 4.8, 6.4, 7, 5.6, 7.3, 6.4)

d = lm(miles_traveled ~ travel_time)

