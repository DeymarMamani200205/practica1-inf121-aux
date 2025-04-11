public class Estudiante {
    private String nombre;
    private double nota1;
    private double nota2;

    public Estudiante(String nombre, double nota1, double nota2) {
        this.nombre = nombre;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }

    public double calcularPromedio() {
        return (this.nota1 + this.nota2) / 2;
    }

    public boolean aprobo() {
        return this.calcularPromedio() >= 6;
    }

    public String getNombre() {
        return this.nombre;
    }

    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("Carlos", 8, 9);
        Estudiante estudiante2 = new Estudiante("Sofía", 4, 7);
        Estudiante estudiante3 = new Estudiante("Pedro", 5, 6);

        System.out.println("Promedio de " + estudiante1.getNombre() + ": " + estudiante1.calcularPromedio() + " - Aprobó: " + estudiante1.aprobo());
        System.out.println("Promedio de " + estudiante2.getNombre() + ": " + estudiante2.calcularPromedio() + " - Aprobó: " + estudiante2.aprobo());
        System.out.println("Promedio de " + estudiante3.getNombre() + ": " + estudiante3.calcularPromedio() + " - Aprobó: " + estudiante3.aprobo());
    }
}