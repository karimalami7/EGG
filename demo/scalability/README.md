# Scalability

Scalability aims to evaluate performance of **EGG** in generating evolving graphs, compared to # of nodes and # of snapshots.

To run a scalability test, first define the values of the parameters (# of nodes and # of snapshots) in the file scalcalc.pl

```perl
	my $size=30;
	my %interval=("d"=>10,"f"=>100,"m"=>2);
  
	my $interval=10;
	my %size=("d"=>10,"f"=>10000,"m"=>10);
```

Then run the script associated to each use case, for example, to evaluate scalability of **EGG** with *social* use case, run the following command:

```shell
./shell_social
```

Two csv files will be generated, containing the varying parameter, and the execution time of **EGG**.

[egg-fixed-interval-to-100-social.txt](https://github.com/karimalami7/EGG/blob/master/demo/scalability/egg-fixed-interval-to-100-social.txt)

[egg-fixed-size-to-100000-social.txt](https://github.com/karimalami7/EGG/blob/master/demo/scalability/egg-fixed-size-to-100000-social.txt)

Then you can plot the results by calling [plot_scal.py](https://github.com/karimalami7/EGG/blob/master/demo/scalability/plot_scal.py) script, mentioning a csv file without the .txt extension:

```python 
python plot.py egg-fixed-interval-to-100-social
```
