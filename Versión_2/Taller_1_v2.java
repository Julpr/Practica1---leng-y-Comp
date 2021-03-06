import java.io.*;

import java.text.Normalizer;
import java.util.Arrays;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

/*
 	Class: Taller_1
 	
 	Title:	Integrantes
 	-  Maribel Orozco Alzate.
	-  Julián Patiño Rincón.
 */
public class Taller_1_v2 {
	public String VecAritm[]= {};
	
	//Atributos
	//Se creó un arreglo vació que irá guardando cada palabra que se encuentra en el fichero
	public String palabras[]= {}; 
	//Obtienen la posición de cada caracter (ubicacionX) y el número de cada línea(ubicacionY)
	public int[] ubicacionX= {}; 
	public int[] ubicacionY= {};
	//Tabla final con Símbolo, Ubicación y tipos
	public String[][] tabla, aritmetica; 

	public static void setTabla(String[][] tabla, int f, int c, String s) {
		tabla[f][c] = s;
	}

	public String[] getTabla() {
		return palabras;
	}
	
	public int[] getUbicacion() {
		return ubicacionX;
	}
	
	//Se crea una matriz de 2 filas por 36 columnas, en las cuales se guarda los símbolos y su respectivo tipo 
	private String [][] simbolos= {{"espacio","tab","+","-","*","/","%",">","<",",","=","(",")","{","}",
		"[","]","for","while","for","while","if","else If","else","if","else If","else","class",
		"def","print","default","break","return","int","char","string",},

			{"Separador","Tab","Operador arimetico",
			"Operador arimetico","Operador arimetico","Operador arimetico","Operador arimetico",
			"Operador Relacional","Operador Relacional","Operador Relacional","Operador Relacional",
			"Operador de agrupación","Operador de agrupación","Operador de agrupación",
			"Operador de agrupación","Operador de agrupación","Operador de agrupación","Ciclos","Ciclos",
			"Palabra reservada","Palabra reservada","Condicional","Condicional","Condicional",
			"Palabra reservada","Palabra reservada","Palabra reservada","Palabra reservada",
			"Palabra reservada","Palabra reservada","Palabra reservada",
			"Palabra reservada","Palabra reservada","Palabra reservada","Palabra reservada","Palabra reservada"}};
	
/*
   		Function: imprimirVector
   
  		Imprime cada uno de los elementos de un vector
  
  		Parameters:
  		array - Vector a imprimir posteriormente 
 
 */
	public static void imprimirVector(String[] array) {
		for(String i:array)
			System.out.print("  "+i+"   	");
		System.out.println();
	}
/*
  		Function: imprimirMatriz
  
  		Imprimirá por consola cada uno de los elementos de la matriz que contiene la clase "Taller_1"
 */
	public void imprimirMatriz() {
		for(int i=0; i<tabla.length;i++) {
			for(int j=0; j<4;j++) {
				System.out.print(tabla[i][j]+"  		   ");
			}
			System.out.println();
		}
	}
	
/*
  		Function: addElemento
  
  		Aumenta la longitud del arreglo "palabras" para añadir más elementos 
  
  		Parameters:
   		S - Cadena que se agregará al arreglo 
 
 */
	public static String[] addElemento(String S, String[] array) {
		//Se utiliza el metodo "copyOf" de la clase "Arrays" para hacer una copia del arreglo y aumentar su longitud
		array=Arrays.copyOf(array, array.length+1);
		//Se agrega el elemento a la última posisión del arreglo
		array[array.length-1]=S;
		
		return array;
	}
	
/*
  		Function: crearTabla
  	
  		Redimensiona la matriz "Tabla" en Function de la longitud del arreglo "Palabras". Ambos son atributos de la clase: "Taller_1"
 
 */
	public void crearTabla() {
		this.tabla= new String[palabras.length+1][4];	
	}
	
/*
  		Function: tipoSimbolos
  
  		Recorre el arreglo de palabras para comparar cada uno de los elementos de este con los de la matriz "simbolos" e 
  		identificar su tipo.
 */
	public void tipoSimbolos() {
		int k=0;
		//Recorre la matriz "Tabla"
		for (int i = 1; i < tabla.length-1; i++) {
			//Recorre la matriz de "simbolos" en la fila con índice 0 para comparar los caracteres o palabras
			for (int j = 0; j < simbolos[0].length; j++) {
				//Verifica si la palabra de posición actual es igual al simbolo de la posición actual
				 if(tabla[i][0].compareToIgnoreCase(simbolos[0][j])==0) {
					 	//Comprueba que la casilla esté vacía para agregar el correspondiente tipo
						if(tabla[i][2]==null) {
							tabla[i][2]=simbolos[1][j];
						}
						//En caso de que la casilla esté llena y con un tipo de símbolo diferente al que se analiza
						//En la posición actual se agrega el otro tipo a la columna de índice 3.
						if(tabla[i][2]!=null && tabla[i][2]!=simbolos[1][j]){
							tabla[i][3]=simbolos[1][j];
						}
				  } 
					  
				k=j;
			}
			
			//En caso de que el caracter o la palabra analizada no se encuentre en la matriz de "simbolos", esta será
//			//clasificada como de tipo "Identificador"
			 if((k==simbolos[0].length-1) && tabla[i][1]!=null) {
				 tabla[i][2]="Identificador";
			 }
		}
	}
	
/*
  		Function: llenarTabla
  
  		Llena la tabla que se mostrará al final. La primera columna corresponde a las palabras, caracteres y espacios
  		que se encuentran en el archivo y se obtienen del arreglo "Palabras".
 		La segunda columna es llenada con las posiciones de cada caracter y su respectiva linea.
 		La tercera columna se iniciliza con espacios en blanco.
  
 */
	public void llenarTabla() {
		int cont=0;
		tabla[0][0]="Símbolos";
		tabla[0][1]="Ubicación";
		tabla[0][2]="Tipo-1";
		tabla[0][3]="Tipo-2";
		for(int i=1; i<tabla.length; i++) {
			tabla[i][0]=palabras[cont];
			cont++;
		}
		
		for(int i=1; i<tabla.length-1;i++) {
			//En la segunda columna (de índice 1) se agregan las posiciones como duplas (x,y)
			tabla[i][1]="("+ubicacionY[i]+","+ubicacionX[i]+""+")";
			tabla[i][3]=" ";
		}
		
		//Se hace el llamado al método "tipoSimbolos" 
		tipoSimbolos();
	}

/*
  		Function: addUbicacion
  
  		Agrega a los arreglos correspondientes, la ubicación de cada caracter y su respectiva linea.
  
  		Parameters:
  		x - Corresponde a la posición del caracter
  		y - Corresponde a la posición del caracter según la linea
 */
	
	public void addUbicacion(int x, int y) {
		//Se redimensiona el arreglo "ubicaciónX" para posteriormente, agregar un nuevo elemento
		//en su última posición
		ubicacionX=Arrays.copyOf(ubicacionX, ubicacionX.length+1);
		ubicacionX[ubicacionX.length-1]=x;
		//Se redimensiona el arreglo "ubicaciónY" para posteriormente, agregar un nuevo elemento 
		//en su última posición
		ubicacionY=Arrays.copyOf(ubicacionY, ubicacionY.length+1);
		ubicacionY[ubicacionY.length-1]=y;
	}
	
/*
  		Function: quitarSimbolos
  
  		Recibe la palabra la cual será analizada para quitarle caracteres especiales
  
  		Parameters:
  		palabra - palabra que será analizada y posteriormente modificada
  
 		salida:
 		Palabra modificada, libre de caracteres especiales
 */
	public String quitarSimbolos(String palabra) {
		//Normaliza la palabra para quitarle tildes y convertir todas sus letras en minúsculas
		palabra = Normalizer.normalize(palabra, Normalizer.Form.NFD);
		//Se le quitan todos los caracteres especiales
		palabra=palabra.replaceAll("[\\¡!¿?_/=''#$%&(),<>-]", "");
		return palabra;
	}

/*
 		Function:  IndicadorCaracteres
 
 		Nos indica si la palabra contiene o no caracteres especiales
 
 		Parameters:
 		palabra - palabra a analizar
 
 		Salida:
 		Caracter especial o nada, en su defecto
 
 		
 */
	public String IndicadorCaracteres(String palabra){
		int aux=-1;
			//Analiza los 17 primeros símbolos de la matriz "simbolos" que son los caracteres
			//tentativos que la palabra podría tener
			for(int i=0; i<17; i++) {
				//Se verifica si la palabra contiene algún de los símbolos
				if(palabra.contains(simbolos[0][i])) {
					//Variable auxiliar para conocer el caracter 
					aux=i;					
				}
			}
			
			return (aux!=-1)? simbolos[0][aux]:"";
	}
	
	public boolean aritmetic(String c1) {
		int index=0;
		String[] arreglo= {};
		String cadena="";
		while(index<c1.length() && (c1.compareTo("+")!=0 || c1.compareTo("-")!=0 || c1.compareTo("*")!=0 || c1.compareTo("/")!=0)) {
			while(index<c1.length()-1 && (c1.charAt(index)!='+' || c1.charAt(index)!='-' || 
					c1.charAt(index)!='*' || c1.charAt(index)!='/')) {
				
				cadena=cadena+c1.charAt(index);
				index++;
			}
			arreglo=addElemento(cadena, arreglo);
			arreglo=addElemento(c1.charAt(index)+"", arreglo);
			cadena="";
			index++;
		}
		arreglo=Arrays.copyOf(arreglo, arreglo.length-1);
		return verificarAritmetico(arreglo);
	}
	
	public boolean verificarAritmetico(String[] s) {
		boolean aux=false;
		for(int i=1;i<s.length;i=i+2) {
			if(s[i].equals("+") || s[i].equals("-") || s[i].equals("*") || s[i].equals("/")) {
				aux=true;
			}
		}
		
		return (aux==true)? true:false;
	}
	
	static void printVector(String[] v) {
		for(String x:v) {
			System.out.print(x+ " ");
		}
		System.out.println("");
	}
	
/*
  		Function: leerFichero
  
  		Lee un fichero de texto. Lee caracter por caracter contándolos y formando cada una de las palabras
  		que se encuentra en el fichero y se almacenarán en el arreglo "Palabras", donde también almacena 
  		símbolos, espacios y su ubicación
 */

	private void leerFichero() {
		int aux=0;
		
//		//Se crea un objeto de tipo JFileChooser
//		JFileChooser fc=new JFileChooser("../");
//		fc.showOpenDialog(null);
//		
//		//Se crea el objeto file con la ruta del archivo que fue seleccionado con el JFileChooser
//		File f=new File(fc.getSelectedFile().toString());

		//ESTO SE ELIMINAAA (ES PROVISIONAL PARA NO TENER QUE ESTAR ELIGIENDO EL ARCHIVO MIENTRAS SE HACEN PRUEBAS
		File f=new File("src/Archivo.txt"); 
		
		FileReader fr=null;
		BufferedReader b=null;

		try {
			fr= new FileReader(f);
			b= new BufferedReader(fr);

			int linea;
			//palabra: Auxiliar para crear palabras que serán guardadas en el arreglo "Palabras"
			String palabra=""; 
			//Es un auxiliar que me permite analizar si la palabra contiene caracteres especiales y eliminarlos sin alterar la palabra original
			String copiaPalabra="";
			//Contador para conocer las ubicaciones de los caracteres
			int contUb=0;
			//Contador para conocer las ubicacion de la linea
			int contlinea=1;
			
			//Verifica cuando se llega al final del archivo
			while((linea=b.read())!=-1) {
				aux=0;				
				contUb++;
				
				//Acumula los caracteres hasta que encuentra un espacio que indica la formación de una palabra
				while((char)linea!=' ' && aux!=-1) {
					palabra+=(char)linea;
					aux=-1;
				}
				
				//Detecta el salto de linea (10 en el código ASCII)
				if(linea==10) {
					//Se reinicia el contado de carácteres para que en cada salto de línea comience desde 1
					contUb=1;
					//Se aumenta el contador de saltos de línas
					contlinea++;
				}
				
				if((char)linea==' ') {
					//Se hace el llamado de algunos métodos que ya fueron explicados anteriormente
					copiaPalabra=palabra;
					palabras=addElemento(quitarSimbolos(palabra), palabras);
					addUbicacion((contUb-palabra.length()), contlinea);
					
					if(aritmetic(quitarSimbolos(palabra))) {
						VecAritm=addElemento(quitarSimbolos(palabra), VecAritm);
					}
					
					if(IndicadorCaracteres(copiaPalabra)!="") {
						palabras=addElemento(IndicadorCaracteres(copiaPalabra), palabras);
						addUbicacion(contUb-1, contlinea);
					}
					palabras=addElemento("espacio", palabras);
					addUbicacion(contUb,contlinea);
					
					quitarSimbolos(palabra);
					palabra="";
					copiaPalabra="";
				}
			}

			copiaPalabra=palabra;
			palabras=addElemento(quitarSimbolos(palabra), palabras);
			addUbicacion((contUb-palabra.length()),contlinea);
			
			if(IndicadorCaracteres(copiaPalabra)!="") {
				palabras=addElemento(IndicadorCaracteres(copiaPalabra), palabras);
				addUbicacion(contUb-1,contlinea);
			}
			
			quitarSimbolos(palabra);
			
			palabra="";
			copiaPalabra="";
			
			crearTabla();

		}catch(FileNotFoundException e) {
			System.out.println("No se pudo encontrar el fichero");
		}catch(IOException e) {
			System.out.println("No se pudo leer el fichero");
		}finally {
			try {
				if(fr!=null) {
					b.close();
					fr.close();
				}
			}catch(IOException e){
				System.out.println("No se pudo cerrar el fichero");
			}
		}

	}
	
	public static void main(String[] args) {
		//Se instancia la clase "Taller_1"
		Taller_1_v2 t=new Taller_1_v2();
		//Se hace llamado de los siguentes métodos
		t.leerFichero();
		t.llenarTabla();
		t.tipoSimbolos();
//		t.imprimirMatriz();
		System.out.println("\n\n");
		printVector(t.VecAritm);
		System.out.println("       Long VecAritm "+t.VecAritm.length);
	}
}
