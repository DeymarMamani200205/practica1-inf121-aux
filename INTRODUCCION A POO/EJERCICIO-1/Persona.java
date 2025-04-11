public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public String mostrarSaludo() {
        return "Hola, soy " + this.nombre + " de " + this.ciudad;
    }

    public boolean esMayorDeEdad() {
        return this.edad >= 18;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Ana", 25, "Madrid");
        Persona persona2 = new Persona("Luis", 16, "Barcelona");
        Persona persona3 = new Persona("Sofía", 30, "Valencia");

        System.out.println(persona1.mostrarSaludo());
        System.out.println(persona2.mostrarSaludo());
        System.out.println(persona3.mostrarSaludo());
    }
}