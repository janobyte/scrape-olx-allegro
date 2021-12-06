library(readr)
library(tidyverse)
library(psych)

df <- read_csv('output.csv')
df2 <- filter(df, price>=500)

x = df2$price
hist(x, main = mtext(bquote(
  paste(bolditalic("median") == .(round(median(x),1)), " (",
        bolditalic("mean") == .(round(mean(x),1)), ")")
)), xlab = "Price Distribution", xlim=range(x), prob=TRUE)
rug(x)
abline(v = median(x), col = "red", lwd=2)
lines(density(x))

summary(x)
describe(x)
