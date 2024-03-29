package model.ADT;
import model.exception.ADTException;

import java.util.*;

public class MyStack<T> implements IMyStack<T> {
    private Stack<T> stack;

    public MyStack(){
        this.stack = new Stack<T>();
    }
    @Override
    public T pop() throws ADTException {
        if (stack.isEmpty())
            throw new ADTException("The stack is empty");
        return stack.pop();
    }

    @Override
    public void push(T v) {
        this.stack.push(v);
    }

    @Override
    public boolean isEmpty() {
        return (this.stack.isEmpty());
    }

    @Override
    public Stack<T> getContent() {
        return this.stack;
    }

    @Override
    public List<T> getReversed() {
        List<T> list = Arrays.asList((T[]) stack.toArray());
        Collections.reverse(list);
        return list;
    }

    @Override
    public String toString() {
        String representation = "";
        for(int i = stack.size() - 1; i >= 0; i--){
            representation += stack.get(i).toString() + "\n";
        }
        return representation;

    }


}
