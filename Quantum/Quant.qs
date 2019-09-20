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
		using (q = Qubit())
		{
			H(q);
			if(M(q)==Zero)
			{
				Message("It was zero!");
			} else {
				Message("It was one!");
			}
			// elif
			
			Reset(q);
		}
	}
	
}
