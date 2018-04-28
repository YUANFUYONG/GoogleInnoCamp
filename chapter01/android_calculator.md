####android计算器代码

```
Android计算器业务逻辑代码
```
    public class CalculatorActivity extends AppCompatActivity implements View.OnClickListener {
   
    private Button btn_0;
    private Button btn_1;
    private Button btn_2;
    private Button btn_3;
    private Button btn_4;
    private Button btn_5;
    private Button btn_6;
    private Button btn_7;
    private Button btn_8;
    private Button btn_9;
    private Button btn_equal;
    private Button btn_point;
    private Button btn_clean;
    private Button btn_del;
    private Button btn_plus;
    private Button btn_minus;
    private Button btn_multiply;
    private Button btn_divide;
    private TextView et_input;
    boolean clear_flag;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calculator);
        intitView();
        intitEvent();
    }

    /**
     * 初始化控件
     */
    private void intitView() {
        btn_0 = (Button) findViewById(R.id.btn_0);
        btn_1 = (Button) findViewById(R.id.btn_1);
        btn_2 = (Button) findViewById(R.id.btn_2);
        btn_3 = (Button) findViewById(R.id.btn_3);
        btn_4 = (Button) findViewById(R.id.btn_4);
        btn_5 = (Button) findViewById(R.id.btn_5);
        btn_6 = (Button) findViewById(R.id.btn_6);
        btn_7 = (Button) findViewById(R.id.btn_7);
        btn_8 = (Button) findViewById(R.id.btn_8);
        btn_9 = (Button) findViewById(R.id.btn_9);
        btn_clean = (Button) findViewById(R.id.btn_clean);
        btn_equal = (Button) findViewById(R.id.btn_equal);
        btn_minus = (Button) findViewById(R.id.btn_minus);
        btn_multiply = (Button) findViewById(R.id.btn_multiplay);
        btn_plus = (Button) findViewById(R.id.btn_plus);
        btn_point = (Button) findViewById(R.id.btn_point);
        btn_del = (Button) findViewById(R.id.btn_del);
        btn_divide = (Button) findViewById(R.id.btn_divide);
        et_input = (TextView) findViewById(R.id.et_input);
    }

    /**
     * 初始化事件
     */
    private void intitEvent() {
        btn_0.setOnClickListener(this);
        btn_1.setOnClickListener(this);
        btn_2.setOnClickListener(this);
        btn_3.setOnClickListener(this);
        btn_4.setOnClickListener(this);
        btn_5.setOnClickListener(this);
        btn_6.setOnClickListener(this);
        btn_7.setOnClickListener(this);
        btn_8.setOnClickListener(this);
        btn_9.setOnClickListener(this);
        btn_equal.setOnClickListener(this);
        btn_minus.setOnClickListener(this);
        btn_multiply.setOnClickListener(this);
        btn_divide.setOnClickListener(this);
        btn_del.setOnClickListener(this);
        btn_point.setOnClickListener(this);
        btn_plus.setOnClickListener(this);
        btn_clean.setOnClickListener(this);
        et_input.setOnClickListener(this);
    }

    /**
     * 点击事件
     *
     * @param view 点击的控件
     */
    @Override
    public void onClick(View view) {
        String str = et_input.getText().toString();
               switch (view.getId()) {
                   case R.id.btn_0:
                   case R.id.btn_1:
                   case R.id.btn_2:
                   case R.id.btn_3:
                   case R.id.btn_4:
                   case R.id.btn_5:
                   case R.id.btn_6:
                   case R.id.btn_7:
                   case R.id.btn_8:
                   case R.id.btn_9:
                       //小数点
                   case R.id.btn_point:
                       if (clear_flag) {
                           clear_flag = false;
                           str = "";
                           et_input.setText("");
                       }
                       et_input.setText(str + ((Button) view).getText());
                       break;
                   //加号
                   case R.id.btn_plus:
                       //减号
                   case R.id.btn_minus:
                       //乘号
                   case R.id.btn_multiplay:
                       //除号
                   case R.id.btn_divide:
                       if (clear_flag) {
                           clear_flag = false;
                           str = "";
                           et_input.setText("");
                       }
                       et_input.setText(str + " " + ((Button) view).getText() + " ");
                       break;
                   case R.id.btn_clean:
                       clear_flag = false;
                       et_input.setText("");
                       break;
                   //删除
                   case R.id.btn_del:
                       if (clear_flag) {
                           clear_flag = false;
                           et_input.setText("");
                       } else if (str != null && !str.equals("")) {
                           et_input.setText(str.substring(0, str.length() - 1));
                       }
                       //等号
                   case R.id.btn_equal:
                       getResult();
                       break;
                   default:
                       break;
               }
    }

      /**
         * 单独的调用运算结果
         */
        private void getResult() {
            //显示运算结果
            String exp = et_input.getText().toString();
            if (exp == null || exp.equals("")) {
                return;
            }
            if (!exp.contains(" ")) {
                return;
            }
            if (clear_flag) {
                clear_flag = false;
                return;
            }
            clear_flag = true;
            double result = 0;
            String s1 = exp.substring(0, exp.indexOf(" "));//输入的第一个数
            String op = exp.substring(exp.indexOf(" ") + 1, exp.indexOf(" ") + 2);//输入的中间符号
            String s2 = exp.substring(exp.indexOf(" ") + 3);//输入的第二个数
            if (!s1.equals("") && !s2.equals("")) {
                double d1 = Double.parseDouble(s1);//第一个数
                double d2 = Double.parseDouble(s2);//第二个数
                if (op.equals("+")) {
                    //进行加运算
                    result = d1 + d2;
                } else if (op.equals("-")) {
                    //进行减运算
                    result = d1 - d2;
                } else if (op.equals("*")) {
                    //进行乘运算
                    result = d1 * d2;
                } else if (op.equals("/")) {
                    //进行除运算
                    if (d2 == 0) {
                        //除数为0，则结果为0,不进行判断就会出错
                        result = 0;
                    } else {
                        result = d1 / d2;
                    }
                }
                //判断第一个数、第二个数里面没有小数点、中间的符号没有除号，最后结果为整数
                if (!s1.contains(".") && !s2.contains(".") && !op.equals("/")) {
                    int r = (int) result;
                    et_input.setText(r + "");
                } else {
                    et_input.setText(result + "");
                }
                //第一个数不为空，第二个数为空
            } else if (!s1.equals("") && s2.equals("")) {
                et_input.setText(exp);
                //第一个数为空，第二个数不为空，可以把第一个数看成0
            } else if (s1.equals("") && !s2.equals("")) {
                double d2 = Double.parseDouble(s2);
                if (op.equals("+")) {
                    result = 0 + d2;
                } else if (op.equals("-")) {
                    result = 0 - d2;
                } else if (op.equals("*")) {
                    result = 0;
                } else if (op.equals("/")) {
                    result = 0;
                }
                //第二数中不包含.，则第二个数为整数
                if (!s2.contains(".")) {
                    int r = (int) result;
                    et_input.setText(r + " ");
                } else {
                    et_input.setText(result + " ");
                }
            } else {
                et_input.setText("");
            }
        }
     }
 
 
```
Android计算器页面布局
```
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/et_input"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_gravity="end"
        android:layout_weight="1"
        android:padding="20dp"
        android:singleLine="true"
        android:textAlignment="textEnd"
        android:textSize="30sp" />

    <TableLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TableRow
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <!--第一行-->
            <Button
                android:id="@+id/btn_clean"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="C"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_del"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="Del"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_divide"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="/"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_multiplay"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="*"
                android:textSize="20sp" />
        </TableRow>

        <!--第二行-->
        <TableRow>

            <Button
                android:id="@+id/btn_7"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="7"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_8"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="8"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_9"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="9"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_minus"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="-"
                android:textSize="20sp" />
        </TableRow>


        <!--第三行-->
        <TableRow>

            <Button
                android:id="@+id/btn_4"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="4"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_5"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="5"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_6"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="6"
                android:textSize="22sp" />

            <Button
                android:id="@+id/btn_plus"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="+"
                android:textSize="20sp" />
        </TableRow>

        <!--第四行-->
        <TableRow>

            <Button
                android:id="@+id/btn_0"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="0"
                android:textSize="20sp" />

            <Button
                android:id="@+id/btn_1"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="1"
                android:textSize="20sp" />

            <Button
                android:id="@+id/btn_2"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="2"
                android:textSize="20sp" />

            <Button
                android:id="@+id/btn_3"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="3"
                android:textSize="20sp" />
        </TableRow>

        <!--第五行-->
        <TableRow>

            <Button
                android:id="@+id/btn_point"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="."
                android:textSize="20sp" />

            <Button
                android:id="@+id/btn_equal"
                android:layout_width="0dp"
                android:layout_height="72dp"
                android:layout_weight="1"
                android:text="="
                android:textSize="20sp" />
        </TableRow>

    </TableLayout>
    </LinearLayout>






