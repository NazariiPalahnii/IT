program Calculator;

var 
  a, b, d, calNumber: integer;
  calShow: string;

function number(a, b, d: integer): integer;

begin // function number

  if d = 1 then
    number := a + b
  else if d = 2 then
    number := a - b
  else if d = 3 then
    number := a div b
  else if d = 4 then
    number := a * b
  else
    number := 0; 

end;

function operators: string;

begin // function operators
  if d = 1 then
    operators := ' + '
  else if d = 2 then
    operators := ' - '
  else if d = 3 then
    operators := ' / '
  else if d = 4 then
    operators := ' * '
  else
    operators := ' ? '; 
end;

begin // main body
  writeln('1. Plus');
  writeln('2. Minus');
  writeln('3. Divide');
  writeln('4. Multiply');
  write('What operators do you want use? (type a number): ');
  readln(d);

  write('Enter a number_1: ');
  readln(a);

  write('Enter a number_2: ');
  readln(b);
  
  calNumber := number(a, b, d);
  calShow := operators;
  writeln(a, calShow, b, ' = ', calNumber);
end.
