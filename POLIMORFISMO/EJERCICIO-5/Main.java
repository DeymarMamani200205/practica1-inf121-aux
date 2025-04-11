abstract class Ambiente {
    protected String nombre;

    public Ambiente(String nombre) {
        this.nombre = nombre;
    }

    public abstract void mostrar();

    public abstract int cantidadMuebles();

    @Override
    public String toString() {
        return "Ambiente: " + nombre;
    }
}

class Oficina extends Ambiente {
    private int nroSillas;
    private int nroEscritorios;
    private int nroEstantes;

    public Oficina(String nombre, int nroSillas, int nroEscritorios, int nroEstantes) {
        super(nombre);
        this.nroSillas = nroSillas;
        this.nroEscritorios = nroEscritorios;
        this.nroEstantes = nroEstantes;
    }

    @Override
    public void mostrar() {
        System.out.println("Oficina: " + nombre + ", Sillas: " + nroSillas + ", Escritorios: " + nroEscritorios + ", Estantes: " + nroEstantes);
    }

    @Override
    public int cantidadMuebles() {
        return nroSillas + nroEscritorios + nroEstantes;
    }
}

class Aula extends Ambiente {
    private int capacidad;
    private int nroPupitres;

    public Aula(String nombre, int capacidad, int nroPupitres) {
        super(nombre);
        this.capacidad = capacidad;
        this.nroPupitres = nroPupitres;
    }

    @Override
    public void mostrar() {
        System.out.println("Aula: " + nombre + ", Capacidad: " + capacidad + ", Pupitres: " + nroPupitres);
    }

    @Override
    public int cantidadMuebles() {
        return nroPupitres;
    }
}

class Laboratorio extends Ambiente {
    private int capacidad;
    private int nroMesas;
    private int nroSillas;

    public Laboratorio(String nombre, int capacidad, int nroMesas, int nroSillas) {
        super(nombre);
        this.capacidad = capacidad;
        this.nroMesas = nroMesas;
        this.nroSillas = nroSillas;
    }

    @Override
    public void mostrar() {
        System.out.println("Laboratorio: " + nombre + ", Capacidad: " + capacidad + ", Mesas: " + nroMesas + ", Sillas: " + nroSillas);
    }

    @Override
    public int cantidadMuebles() {
        return nroMesas + nroSillas;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Instanciando ambientes ===");
        Oficina oficina1 = new Oficina("Oficina A", 5, 3, 2);
        Oficina oficina2 = new Oficina("Oficina B", 4, 2, 1);
        Aula aula1 = new Aula("Aula 101", 30, 30);
        Aula aula2 = new Aula("Aula 102", 25, 25);
        Laboratorio laboratorio1 = new Laboratorio("Lab Química", 20, 10, 20);

        Ambiente[] ambientes = {oficina1, oficina2, aula1, aula2, laboratorio1};

        System.out.println("\n=== Datos de cada ambiente ===");
        for (Ambiente ambiente : ambientes) {
            ambiente.mostrar();
        }

        System.out.println("\n=== Cantidad de muebles por ambiente ===");
        int totalMuebles = 0;
        for (Ambiente ambiente : ambientes) {
            int muebles = ambiente.cantidadMuebles();
            System.out.println(ambiente.getClass().getSimpleName() + " " + ambiente.nombre + ": " + muebles + " muebles");
            totalMuebles += muebles;
        }
        System.out.println("\nTotal de muebles en todos los ambientes: " + totalMuebles);
    }
}