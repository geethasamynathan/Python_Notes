# Equivalent of System.Diagnostics.Write in Python

## **1. Equivalent of `System.Diagnostics.Debug.Write` in Python**

### **C# Example**
```csharp
using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        Debug.Write("This is a debug message in .NET");
        Trace.Write("This is a trace message in .NET");
    }
}
```

### **Python Equivalent**
```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Equivalent to Debug.Write
logging.debug("This is a debug message in Python")

# Equivalent to Trace.Write
logging.info("This is an info (trace) message in Python")
```

---

## **2. Equivalent of `System.Diagnostics.Process.GetProcesses()` in Python**

### **C# Example**
```csharp
using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        Process[] processList = Process.GetProcesses();
        foreach (Process proc in processList)
        {
            Console.WriteLine($"Process: {proc.ProcessName}, ID: {proc.Id}");
        }
    }
}
```

### **Python Equivalent**
```python
import psutil

# Get all running processes
for proc in psutil.process_iter(['pid', 'name']):
    print(f"Process: {proc.info['name']}, ID: {proc.info['pid']}")
```

**Note:**  
- The `psutil` module in Python provides an API for retrieving process information similar to `System.Diagnostics.Process` in .NET.
- If `psutil` is not installed, you can install it using:
  ```sh
  pip install psutil
  
