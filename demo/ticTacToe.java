import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

public class ticTacToe {
	public static void main (String[] args)
	{
		//take input for computer vs player
		String s = "Press 1: If want to play with 2 players\n" +
				"Press 2: If want to play with computer \n";
		System.out.println(s);
		Scanner in = new Scanner(System.in);
		int choice = in.nextInt();
		in.nextLine(); //solve the issue;
		//start the game
		Board game = new Board();
		int input;
		boolean set;
		int tmp;
		s= "Player1: Choose H for Heads or T for Tails";
		System.out.println(s);
		String selection = in.nextLine();
		if (choice==2)
			{
				if (selection.equals(toss()))
				{
					System.out.println("Player1 have won the toss, you will go first and your mark is 'o' ");
					while( !game.checkFinish('x') && !game.checkFinish('o') )
					{
						do{
							input=user_input(in,"player 1" );
							set=game.addPosition(input-1,'o');
						}while(!set);
						if (!game.checkFinish('x') && !game.checkFinish('o')){
						tmp=solve_computer(game,'x');
						System.out.println("computer move:"+tmp);
						game.addPosition(tmp-1,'x');
						System.out.print(" The board position after computer move \n");
						System.out.print(game);}
					}
				}else{
					System.out.println("Player1 have not won the toss, computer will go first with its mark as 'x'");
					while( !game.checkFinish('x') && !game.checkFinish('o') )
					{
						tmp=solve_computer(game,'x');
						System.out.println("computer move:"+tmp);
						game.addPosition(tmp-1,'x');
						System.out.print(" The board position after computer move \n");
						System.out.print(game);
						if (!game.checkFinish('x') && !game.checkFinish('o')) {
						do{
							input=user_input(in,"player 1" );
							set=game.addPosition(input-1,'o');
						}while(!set);
						}
					}
				}
			}else {
				if (selection.equals(toss()))
				{
					System.out.println("Player1 have won the toss, Player1 will go first and your mark is 'o' ");
					while( !game.checkFinish('x') && !game.checkFinish('o') )
					{
						do{
							input=user_input(in,"player 1" );
							set=game.addPosition(input-1,'o');
						}while(!set);
						System.out.print(" The board position after player 1 move \n");
						System.out.print(game);
						if(!game.checkFinish('x') && !game.checkFinish('o')) 
						{
							do {
								input=user_input(in,"player 2" );
								set=game.addPosition(input-1,'x');
							}while(!set);
						}
						System.out.print(" The board position after player 2 move \n");
						System.out.print(game);
					}
				}else{
					System.out.println("Player2 have won the toss, Player2 will go first and your mark is 'o' ");
					while( !game.checkFinish('x') && !game.checkFinish('o') )
					{
						do{
							input=user_input(in,"player 2" );
							set=game.addPosition(input-1,'o');
						}while(!set);
						System.out.print(" The board position after player 2 move \n");
						System.out.print(game);
						if(!game.checkFinish('x') && !game.checkFinish('o')) 
						{
							do {
								input=user_input(in,"player 1" );
								set=game.addPosition(input-1,'x');
							}while(!set);
						}
						System.out.print(" The board position after player 1 move \n");
						System.out.print(game);
					}
				}
			}
	}
	
	private static int user_input(Scanner in, String player ){
		System.out.println(player+": input your cell option from 1 to 9");
		int input=in.nextInt();
		return input;
	}
	private static String toss () {
		Random coin = new Random();
		int ans = coin.nextInt(2);
		if (ans==1) {
			return "H";
		}else {
			return "T";
		}
	}
	
	private static char another_mark(char a) {
		if (a=='o'){
			return 'x';
		}else if (a=='x') {
			return 'o';
		}else {
			throw new ArithmeticException("markIssue");
		}

	} 



	private static int solve_computer(Board game, char mark )
	{
		//play to complete your trifecta
		if ((Boolean) game.checkColumn (2 , mark).get(0)) 
		{
			int column = (int) game.checkColumn (2 , mark).get(1);
			if (game.checkEmpty(game.giveColumnBlock(column))){
				return game.toLinear(game.giveColumnBlock(column));}
		}
		if ((Boolean) game.checkRow(2, mark).get(0)) {
			int row = (int) game.checkRow (2 , mark).get(1);
			if (game.checkEmpty(game.giveRowBlock(row))){
				return game.toLinear(game.giveRowBlock(row));}
		} 
		if ( (Boolean) game.checkDiag1(2,mark).get(0)) {
			if (game.checkEmpty(game.giveDiag1Block())){
				return game.toLinear(game.giveDiag1Block());}
		} 
		if ( (Boolean) game.checkDiag2(2,mark).get(0)) {
			if (game.checkEmpty(game.giveDiag2Block())){
				return game.toLinear(game.giveDiag2Block());}
		}
		//check to block 
		if ((Boolean) game.checkColumn (2 , another_mark(mark)).get(0)) 
		{
			int column = (int) game.checkColumn (2 , another_mark(mark)).get(1);
			if (game.checkEmpty(game.giveColumnBlock(column))){
				return game.toLinear(game.giveColumnBlock(column));}
		}
		if ((Boolean) game.checkRow(2,another_mark(mark)).get(0)) {
			int row = (int) game.checkRow (2 , another_mark(mark)).get(1);
			if (game.checkEmpty(game.giveRowBlock(row))){
				return game.toLinear(game.giveRowBlock(row));}
		} 
		if ( (Boolean) game.checkDiag1(2,another_mark(mark)).get(0)) {
			if (game.checkEmpty(game.giveDiag1Block())){
				return game.toLinear(game.giveDiag1Block());}
		}
		if ( (Boolean) game.checkDiag2(2,another_mark(mark)).get(0)) {
			if (game.checkEmpty(game.giveDiag2Block())){
				return game.toLinear(game.giveDiag2Block());}
		}
		 
		//play for corners 
		if (true) 
		{
			int[][] corners = {
								{0,0},
								{2,2},
								{0,2},
								{2,0},
							};
			Random generator= new Random();
			int val;
			do 
			{
				val= generator.nextInt(corners.length);
				if(game.checkEmpty(corners[val])) {
					return game.toLinear(corners[val]);
				}
				corners=remove_row(corners,val);
			} while(corners.length>0);
		}
		if (true) 
		{
			if (game.checkEmptyAny()>0) {
				return game.checkEmptyAny();
			}

		}
		throw new ArithmeticException("solveIssue");
	}
	
	public static int [][] remove_row (int[][] arr, int index){
        int [][] tmp = new int[arr.length-1][arr[0].length];
        int a;
        for (int i = 0 ; i<arr.length;i++){
            for (int j =0; j<arr[0].length;j++){
                if(i!=index){
                    if (i>index){
                        a=i-1;
                    } else {
                        a=i;
                    }
                    tmp[a][j]=arr[i][j];
                }
            }
        }
        return tmp;
    }
}


public class Board {
    private char[][] positions;
	private int size = 3; 

	public Board() {
		this.positions= new char[size][size];
	}
	
	public String toString() 
	{
		String border = "|"+"-"+"|"+"-"+"|"+"-"+"|"+"\n";
		String result = "";
		String a;
		int count =0;
		for (int i =0; i< this.size; i++) 
		{
			String tmp="";
			for (int j =0; j<this.size;j++) 
			{
				if (this.positions[i][j]=='\0')
				{
					a=" ";
				}else {
					a=""+this.positions[i][j];
				}
				 tmp = tmp+"|"+a;
				 count=count+1;
			}
			result=result + tmp + "|"+"\n" +border;
		} 
		result=border+result;
		return result;
	}

	public int toLinear(int[] arr){
		return 3*arr[0]+arr[1]+1;
	}

	public boolean checkEmpty (int[] index) {
		int row = index[0];
		int column=index[1];
		if (row==-1 || column==-1) {
			return false;
		}else if (this.positions[row][column]=='\0') {
		return true;
		}else {
			return false;
			}
	}

	public boolean addPosition (int p, char a) {
		int row= p/3;
		int column = p%3;
		if (this.positions[row][column]=='\0') {
		this.positions[row][column]=a;
		return true;
		}else {
			System.out.println("Invalid Position");
			return false;
			}
	}

	public List<Object> checkRow (int l , char a) {
		for (int i =0; i< this.size; i++)
		{
			int count =0 ;
			for (int j=0;j<this.size; j++)
			{
				if (this.positions[i][j]==a){
					count=count+1;
				}
			}
			if (count>=l) {
				boolean check=true;
				int row = i;
				return Arrays.asList(check,row);
			}
		}
		boolean check=false;
		return Arrays.asList(check,null);
	}
	
	public List<Object> checkColumn (int l , char a) {
		for (int i =0; i< this.size; i++) {
			int count =0 ;
			for (int j=0;j<this.size; j++){
				if (this.positions[j][i]==a){
					count=count+1;
				}
			}
			if (count>=l) {
				boolean check=true;
				int column = i;
				return Arrays.asList(check,column);
			}
		}
		boolean check=false;
		return Arrays.asList(check,null);
	}

	public List<Object> checkDiag1 (int l , char a) 
	{
		int count=0;
		for (int i =0; i< this.size; i++) 
		{
			for (int j=0;j<this.size; j++)
			{
				if (i==j) 
				{
					if (this.positions[i][j]==a)
					{
						count=count+1;
					}
				}
				if (count>=l) 
				{
					boolean check=true;
					int diag=1;
					return Arrays.asList(check,diag);
				}
			}
		}
		boolean check=false;
		return Arrays.asList(check,null); 
	}

	public List<Object> checkDiag2 (int l , char a) 
	{
		int count=0;
		for (int i =0; i< this.size; i++) 
		{
			for (int j=0;j<this.size; j++)
			{
				if (i+j==2) 
				{
					if (this.positions[i][j]==a)
					{
						count=count+1;
					}
				}
				if (count>=l) 
				{
					boolean check=true;
					int diag=2;
					return Arrays.asList(check,diag);
				}
			}
		}
		boolean check=false;
		return Arrays.asList(check,null); 
	}
	public int checkEmptyAny() {
		for (int i =0; i<this.size;i++) {
			for (int j =0; j<this.size; j++) {
				if (this.positions[i][j]=='\0') {
					return 3*i+j+1;
				}
			}
		}
		return 0;
	}

	public boolean checkFinish(char a) {
		if ((Boolean) checkColumn (3 , a).get(0)) 
		{
			return true;
		}else if ((Boolean) checkRow(3,a).get(0)) {
			return true;
		} else if ( (Boolean) checkDiag1(3,a).get(0)) {
			return true;
		}else if ( (Boolean) checkDiag2(3,a).get(0)) {
			return true;
		}else if (checkEmptyAny() == 0) {
			return true;
		}else {
			return false;
		}
	}

	public int[] giveRowBlock(int row){
		int[] a = new int[2];
		for (int i=0; i<this.size; i++){
			if (this.positions[row][i]=='\0')
			{
				a[0]=row;
				a[1]=i;
				return a;
			}	
		}
		a[0]=-1;
		a[1]=-1;
		return a;
	}

	public int[] giveColumnBlock(int column){
		int[] a = new int[2];
		for (int i=0; i<this.size; i++){
			if (this.positions[i][column]=='\0')
			{
				a[0]=i;
				a[1]=column;
				return a;
			}		
		}
		a[0]=-1;
		a[1]=-1;
		return a;
	}	
	
	public int[] giveDiag1Block(){
		int[] a = new int[2];
		for (int i=0; i<this.size; i++){
			if (this.positions[i][i]=='\0')
			{
				a[0]=i;
				a[1]=i;
				return a;
			}		
		}
		a[0]=-1;
		a[1]=-1;
		return a;
	}
	
	public int[] giveDiag2Block(){
		int[] a = new int[2];
		for (int i=0; i<this.size; i++){
			if (this.positions[i][2-i]=='\0')
			{
				a[0]=i;
				a[1]=2-i;
				return a;
			}		
		}
		a[0]=-1;
		a[1]=-1;
		return a;	
	}	

}