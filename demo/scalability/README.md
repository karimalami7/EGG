# Scalability

Scalability aims to evaluate performance of **EGG** in generating evolving graphs, compared to # of nodes and # of snapshots.

To run a scalability test, first define the values of the parameters (# of nodes and # of snapshots) in the file scalcalc.pl

```perl
	my $size=30;
	my %interval=("d"=>10,"f"=>100,"m"=>2);
  
	my $interval=10;
	my %size=("d"=>10,"f"=>10000,"m"=>10);
```

Then run the script associated to each use case, for example, to evaluate scalability of **EGG** with social use case, run the following command:

```shell
./shell_social
```
