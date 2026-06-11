# Defining sizes and duration per algorithm ####
quick_times = c(1.540000e-05, 2.820000e-05, 5.350000e-05, 4.413000e-04, 7.790000e-04, 5.214600e-03)
insertion_times = c(9.299998e-06, 5.350000e-05, 1.683000e-04, 4.606700e-03, 2.121750e-02, 5.386755e-01)
bubble_times = c(1.049999e-05, 9.600000e-05, 3.599000e-04, 1.327840e-02, 5.337260e-02, 1.692980e+00)
sizes = c(10, 50, 100, 500, 1000, 5000)

# Standard Graph ####
par(mfrow = c(1,2))
plot(sizes, quick_times, type ='b', 
     xlab = 'Size', 
     ylab = 'Time',
     xaxt = 'n', 
     col = 'blue', 
     lwd = 2, 
     pch=16,
     main = 'Sorting Algorithms Timing Based On Size')
axis(1, at = sizes)

lines(sizes, insertion_times, type = 'b', col = 'purple',lwd=2, pch=16)
lines(sizes, bubble_times, type = 'b', col = 'violet', lwd=2, pch=16)

legend('bottomright', legend = c('Quick', 'Insertion', 'Bubble'), 
       col = c('Blue', 'Purple', "Violet"),
       pch = 16, lwd =2,
       lty = 1)

# Zoomed in standard graph ####
plot(sizes, quick_times, type ='b', 
     xlab = 'Size',
     ylab = 'Time',
     xaxt = 'n', 
     col = 'blue',
     lwd = 2, 
     pch = 16, 
     ylim = c(0, 0.2),
     main = 'Sorting Algorithms Timing Based On Size
Zoomed In')

lines(sizes, insertion_times, type = 'b', col = 'purple',lwd=2, pch=16)
lines(sizes, bubble_times, type = 'b', col = 'violet', lwd=2, pch=16)

axis(1, at = sizes)

legend('topright', legend = c('Quick', 'Insertion', 'Bubble'), 
       col = c('Blue', 'Purple', "Violet"),
       pch = 16, lwd =2,
       lty = 1)


# Zoomed Log Graph ####
par(mfrow = c(1,1))
plot(sizes, quick_times, type ='b',
     xlab = 'Size', ylab = 'Time (log scale)', 
     xaxt = 'n',
     log = 'y',
     col = 'blue', lwd = 2, pch = 16,
     main = 'Sorting Algorithms Timing Based On Size (Log Zoomed In)')

axis(1, at = sizes)

lines(sizes, insertion_times, type = 'b', col = 'purple', lwd = 2, pch = 16)
lines(sizes, bubble_times, type = 'b', col = 'violet', lwd = 2, pch = 16)

legend('bottomright',
       legend = c('Quick', 'Insertion', 'Bubble'),
       col = c('blue', 'purple', 'violet'),
       pch = 16,
       lwd = 2,
       lty = 1)
