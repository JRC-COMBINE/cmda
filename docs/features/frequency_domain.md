
## Power Spectrum
a periodogram

## Welch Power Spectrum
welch method

## Mean Frequency (MNF)
Mean frequency (MNF) of a spectrum is the center of the distribution of power across frequencies. It is calculated as the sum of product of the power spectrum and the frequency divided by the total sum of the power spectrum. The difintion is as follows:

$$\frac{\displaystyle\sum_{j=1}^{M} f_j P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

where $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

## Median Frequency (MDF)
Median frequency (MDF) is a frequency at which the power spectrum is divided into two parts with equal powers.

$$\displaystyle\sum_{j=1}^{MDF} P_j = \displaystyle\sum_{j=MDF}^{M} P_j$$

where $MDF$ is the median frequency, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

## Variance of Central Frequency (VCF)
Variance of central frequency (VCF) can be defined as the variance of power spectrum amlitudes from its mean frequency:

$$\frac{\displaystyle\sum_{j=1}^{M} P_j(f_j-MNF)^2}{\displaystyle\sum_{j=1}^{M} P_j}$$

where $MNF$ is the mean frequency of the power spectrum, $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

## Peak Frequency
Peak frequency is a frequency at which the maximum of power spectrum occurs:

$$\argmax(P_j) , j=1,...,M$$

where $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

## Power Spectrum Ratio (PSR)
Power spectrum ratio (PSR) is a ratio between the energy around the maximum value of the power spectrum and the whole energy of the power spectrum. It can be computed as follows:

$$\frac{\displaystyle\sum_{j={f_0}-n}^{j={f_0}+n} P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

where $f_0$ is the peak frequency, $n$ is the integral limit, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

# Band Power
Band power is the power spectral density in a specified bandwidth. It can be computed as follows:
$$\displaystyle\sum_{j=f_low}^{j=f_high} P_j$$

if normalize by the total power density:

$$\frac{\displaystyle\sum_{j=f_low}^{j=f_high} P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

where $f_low$ and $f_high$ are the low and high frequency band, $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

# Band Power Standard Deviation

# Band Mean Frequency

# Band Median Frequency

# Spectral Entropy





 

