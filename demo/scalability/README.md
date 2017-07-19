# Scalability

In order to evaluate the scalability of our generator, we have run EGG with several use cases and graphs of increasing sizes (in terms of both # of graph nodes and # of graph snapshots).
Details about our experimental findings are available on our [**EGG** scalability wiki](https://github.com/karimalami7/EGG/wiki/Scalability).
We explain here how to reproduce these results and run further similar experiments.

To run a scalability test, first define the values of the parameters (# of nodes and # of snapshots) in the file scalcalc.pl

```perl
	my $size=30;
	my %interval=("d"=>10,"f"=>100,"m"=>2);
  
	my $interval=10;
	my %size=("d"=>10,"f"=>10000,"m"=>10);
```

Then, run the script associated to each use case e.g., to evaluate scalability of **EGG** with *social* use case, run the following command:

```shell
./shell_social
```
This will generate two csv files, containing the varying parameter and the execution time of **EGG**.
We provide here examples of such csv files:

[egg-fixed-interval-to-100-social.txt](https://github.com/karimalami7/EGG/blob/master/demo/scalability/egg-fixed-interval-to-100-social.txt)

[egg-fixed-size-to-100000-social.txt](https://github.com/karimalami7/EGG/blob/master/demo/scalability/egg-fixed-size-to-100000-social.txt)

Then, to plot the results, run the [plot_scal.py](https://github.com/karimalami7/EGG/blob/master/demo/scalability/plot_scal.py) script, having as parameter the name of a csv file without the .txt extension:

```shell 
python plot.py egg-fixed-interval-to-100-social
```
