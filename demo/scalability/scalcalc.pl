use File::Copy;
use Time::Local;



if ($ARGV[0] eq "size"){

	my $size=30;
	my %interval=("d"=>10,"f"=>20,"m"=>2);

	open my $in,  '<', "../../use_cases/$ARGV[1]/$ARGV[1].xml"      or die "Can't read old file: $!";
	open my $out, '>', "../../use_cases/$ARGV[1]/$ARGV[1].xml.new" or die "Can't write new file: $!";
	while( <$in> ) {
 		s/<nodes>.*<\/nodes>/<nodes>$size<\/nodes>/g;
   	 	print $out $_;
 	}
	close $out;
 	close $in;
	move("../../use_cases/$ARGV[1]/$ARGV[1].xml.new","../../use_cases/$ARGV[1]/$ARGV[1].xml");



	for (my $i=$interval{"d"};$i<=$interval{"f"};$i=$i*$interval{"m"}){
	
		open my $in,  '<', "../../use_cases/$ARGV[1]/$ARGV[1]-config.json"      or die "Can't read old file: $!";
		open my $out, '>', "../../use_cases/$ARGV[1]/$ARGV[1]-config.json.new" or die "Can't write new file: $!";
 
		while( <$in> ) {
			s/"interval":.*,/"interval":$i,/g;
      	print $out $_;
		}
		close $out;
		close $in;
 	
 		move("../../use_cases/$ARGV[1]/$ARGV[1]-config.json.new","../../use_cases/$ARGV[1]/$ARGV[1]-config.json");
     
		print "************************\n";
		print "$i nodes\n";
		chdir ("../$ARGV[1]");
		print "Run EGG\n"; 	
		system("./$ARGV[1]-script.sh") ; 
		print "************************\n";
		chdir("../scalability");
   		calc_time("../egg.log","size",$size,$i);
	}

}




if ($ARGV[0] eq "interval"){


	my $interval=10;
	my %size=("d"=>10,"f"=>30,"m"=>10);

	open my $in,  '<', "../../use_cases/$ARGV[1]/$ARGV[1]-config.json"      or die "Can't read old file: $!";
	open my $out, '>', "../../use_cases/$ARGV[1]/$ARGV[1]-config.json.new" or die "Can't write new file: $!";
	while( <$in> ) {
		s/"interval":.*,/"interval":$interval,/g;
  		print $out $_;
	}
	close $out;
	close $in;

 	move("../../use_cases/$ARGV[1]/$ARGV[1]-config.json.new","../../use_cases/$ARGV[1]/$ARGV[1]-config.json");

	my $i;
	for ($i=$size{"d"};$i<=$size{"f"};$i=$i+$size{"m"}){
	
		open my $in,  '<', "../../use_cases/$ARGV[1]/$ARGV[1].xml"      or die "Can't read old file: $!";
		open my $out, '>', "../../use_cases/$ARGV[1]/$ARGV[1].xml.new" or die "Can't write new file: $!";
		while( <$in> ) {
			s/<nodes>.*<\/nodes>/<nodes>$i<\/nodes>/g;
    		print $out $_;
		}
		close $out;
		close $in;
		move("../../use_cases/$ARGV[1]/$ARGV[1].xml.new","../../use_cases/$ARGV[1]/$ARGV[1].xml");

		print "************************\n";
		print "$i nodes\n";
		chdir ("../$ARGV[1]");
		print "Run EGG\n"; 	
		system("./$ARGV[1]-script.sh") ; 
		print "************************\n";
		chdir("../scalability");	
		calc_time("../egg.log","interval",$interval,$i);

	}

}


sub calc_time{



	($x,$y,$z,$w)=@_;

	open my $file_input,'<',$x;

	my @array_input = <$file_input>;

	$first = shift (@array_input);
	
	if ($first =~ m/(.*)-(.*)-(.*) (.*):(.*):(.*),(.*) Let EGG begin/){

		$year = $1;  $month = $2;   $day = $3;
    	$hour = $4;  $minute = $5;  $second = $6;
    	$hour |= 0;  $minute |= 0;  $second |= 0;  # defaults.
    	$year = ($year<100 ? ($year<70 ? 2000+$year : 1900+$year) : $year);
    	$first = timelocal($second,$minute,$hour,$day,$month-1,$year);  
    	$first=$first+($7*0.001);
   
    }

	while ($lastl = pop	(@array_input)){
	
		if ($lastl =~ m/(.*)-(.*)-(.*) (.*):(.*):(.*),(.*) Ti end/){
	
			$year = $1;  $month = $2;   $day = $3;
    		$hour = $4;  $minute = $5;  $second = $6;
    		$hour |= 0;  $minute |= 0;  $second |= 0;  # defaults.
    		$year = ($year<100 ? ($year<70 ? 2000+$year : 1900+$year) : $year);
    		$lastl = timelocal($second,$minute,$hour,$day,$month-1,$year);  	
			$lastl=$lastl+($7*0.001);
	
	
			$diff = $lastl-$first;
 

			close $file_input; 


			open my $file_output, '>>', "egg-fixed-$y-to-$z-$ARGV[1].txt";

			print $file_output "$w;$diff\n";

			close $file_output;
		
		}
	}

}




