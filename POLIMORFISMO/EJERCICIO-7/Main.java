abstract class Animal {
    protected String nombre;

    public Animal(String nombre) {
        this.nombre = nombre;
    }

    public abstract void hacerSonido();

    public abstract void moverse();

    @Override
    public String toString() {
        return "Animal: " + nombre;
    }
}

class Perro extends Animal {
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        super(nombre);
        this.edad = edad;
        this.raza = raza;
    }

    @Override
    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Guau Guau!");
    }

    @Override
    public void moverse() {
        System.out.println(nombre + " se mueve corriendo.");
    }

    @Override
    public String toString() {
        return "Perro: " + nombre + ", Edad: " + edad + ", Raza: " + raza;
    }
}

class Gato extends Animal {
    private String color;

    public Gato(String nombre, String color) {
        super(nombre);
        this.color = color;
    }

    @Override
    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Miau Miau!");
    }

    @Override
    public void moverse() {
        System.out.println(nombre + " se mueve saltando.");
    }

    @Override
    public String toString() {
        return "Gato: " + nombre + ", Color: " + color;
    }
}

class Pajaro extends Animal {
    private String tipo;

    public Pajaro(String nombre, String tipo) {
        super(nombre);
        this.tipo = tipo;
    }

    @Override
    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Pío Pío!");
    }

    @Override
    public void moverse() {
        System.out.println(nombre + " se mueve volando.");
    }

    @Override
    public String toString() {
        return "Pájaro: " + nombre + ", Tipo: " + tipo;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Instanciando animales ===");
        Perro perro1 = new Perro("Max", 5, "Labrador");
        Gato gato1 = new Gato("Luna", "Gris");
        Pajaro pajaro1 = new Pajaro("Tweety", "Canario");

        Animal[] animales = {perro1, gato1, pajaro1};

        for (Animal animal : animales) {
            System.out.println(animal);
        }

        System.out.println("\n=== Sonidos de los animales ===");
        for (Animal animal : animales) {
            animal.hacerSonido();
        }

        System.out.println("\n=== Movimiento de los animales ===");
        for (Animal animal : animales) {
            animal.moverse();
        }
    }
}