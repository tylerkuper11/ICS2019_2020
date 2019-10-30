namespace ICS.Quantum
{
	open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Canon;
	
	operation HelloWorld(): Unit
	{
		Message("Hello, World!");
	}
	
	operation Hello(name: String): Unit
	{
		Message($"Hello, {name}"); // print("Hello, {}" .format(name))
	}
	
	operation HelloSeward(): Unit
	{
		Hello("Mr. Seward");
	}
	
	operation QubitPlay():Unit
	{
		mutable count = 0;
		let maxCount = 1000;
		
		using(qs[] = Qubit(maxCount)){
		for (i in 1 .. maxCount){
				X(qs[i-1]);
				H(qs[i-1]);
				if(M(qs[i-1])==Zero)
				{
					Message("It was zero!");
				} else {
					Message("It was one!");
					set count += 1; // count = count + 1;
				}
				// elif
				
				Reset(q);
			}
		}
		Message($"There were {maxCount-count} zeroes and {count} ones");
	}
	
}
