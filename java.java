class Conditionals{
    public static void main(String[] args) {
        // Declare
        //dataType variableName = value
        // declare without a value
        // dataType variableName;
        // assign or change
        // variableName = newValue;
        int moonSize = 1923;
        double PI = 3.14;
        boolean isSunny = true;
        char firstLetter = 'a';
        // Strings are a reference data type in java from String class
        String greetings = "Greetings!";
        //option 2 from String class
        String greetingstwo = new String("Take me home!");
        System.out.print("Same Line 1st");
        System.out.println(" I'm 2nd");
        System.out.print("I'm third after a new line! ");
        if (isSunny){
            System.out.print("Hi ");
        } else if (isSunny){
            System.out.print("Nope!");
        } else {
            System.out.print("This Will Not Print");
        }
        while (moonSize < 1925){
            System.out.print(moonSize);
            moonSize += 1;
        }
        System.out.println("Moon Size Increase finished");
    

    do {
        moonSize += 1;
        System.out.println("Before");
        System.out.println(moonSize);
    } while (moonSize < 1925);
    
    String[] myArray = new String[5]; 
    for ( int i = 0; i <= myArray.length; i++){
        System.out.print("Empty");
    }
    for (String x : myArray){
        System.out.print("lmao");
        
        if (x== ""){
            continue;
        }
        break;
    }
    String str1 = "practice java!";
    String str2 = " daily!";
    System.out.println(str1.length());
    String str3 = str1.concat(str2);
    System.out.println(str3);
    System.out.println(str2.equals(" daily!"));
    System.out.println(str1.indexOf("t"));
    System.out.println(str1.charAt(4));
    System.out.println(str1.substring(2,10));
    System.out.println(str1.toUpperCase());

}
}
class Whale {
    String whaleSpecies;
    int whaleWeight;
    
    public Whale(String name, int weight) {
      whaleSpecies = name;
      whaleWeight = weight;
    }
  
    public String toString(){
      return "This is a " + whaleSpecies + " whale which weighs about " + whaleWeight + " pounds.";
    }
    
    public static void main(String[] args){
      Whale whale1 = new Whale("narwhal", 2100);
      Whale whale2 = new Whale("beluga", 3000);
      System.out.println(whale1);
      System.out.println(whale2);
    }
  }
class Lists{
    public static void main(String[] args){
        ArrayList<Integer> myList = new ArrayList<Integer>();
        ArrayList<String> months = new ArrayList<String>(12);
        LinkedList<String> days = new LinkedList<String>();
        //ArrayLists are objects without direct indexes
        // use .add .remove (takes in index,item)
        HashMap<String, Integer> tea = new HashMap<>();
        // Hashmap has .put and .get and  .replace
        for (String key: tea.keySet()){
            System.out.println("Brew " + key + " tea at " + tea.get(key) + "*F")
        }
        //False
        tea.containsKey("Abc"); 
        // Hashmaps has .keySet() and .values()
        int[] array = new int[5];
        Set<String> colors = new HashSet<String>();
        // .add .remove .addAll(union) .retainAll (intersection)
        // .removeAll (complement- removes all you can)
        
    }
}