# starting to play with R
t = 2.776445

library(reticulate)
linreg <- import("linear_regression")

tips = linreg$l1
bills = linreg$l2

b <- lm(tips~bills)
sm = summary(b)

sb1 <- sm$sigma/sqrt(sum((bills-mean(bills))^2)) # same thing as coef(sm)[4]

b1 <- coef(b)[2]

mult = sb1 * t

confidence_interval_sl = c(b1+mult, b1-mult) # confidence interval for the *slope*

# rl = abline(b)

predict_singular <- function(linear_model, value) {
    coefficients <- linear_model$coefficients
    result <- coefficients[1] + coefficients[2] * value
    return(result)
}

# x* = the value of interest for the dependent value x
# y* = the possible values y may take when x = x*
# E(y*) = expected or mean value of y when x=x*
# ŷ = b0 + b1 * x*
# ŷ* +/- t_sub(a)/2^S_sub(ŷ*)

yhat_std_d <- function(linear_model, indep_var, value) {
    sm = summary(linear_model)
    sigma = sm$sigma
    numerator = (value - mean(indep_var))^2  # (x* - xbar)^2
    denominator = sum((bills-mean(bills))^2) # python3.7-equivalent: sum([(i - mean(x))**2 for i in x])
    bigroot = sqrt(1/length(indep_var) + (numerator/denominator))
    result <- sigma * bigroot
    return(result)
}

# we can predict with higher precision as x* approaches xbar
# being the precision the highest when x* = xbar
# as s_sub(ŷ*) = s * sqrt(1/n), since x*-xbar = 0

get_confidence_interval <- function(linear_model, indep_var, value, t_value) {
    yhat = predict_singular(linear_model, value)
    standard_deviation = yhat_std_d(linear_model, indep_var, value)
    mult <- t_value * standard_deviation
    result <- c(yhat - mult, yhat + mult) 
    return(result)
}

# get confidence intervals for all values

lower <- c()
higher <- c()
n = 1

for (i in bills) {
    a = get_confidence_interval(b, bills, i, t)
    lower[[n]] <- a[1]
    higher[[n]] <- a[2] 
    n <- n + 1
}
