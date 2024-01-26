package model.ADT;

import model.exception.ADTException;

import java.util.ArrayDeque;
import java.util.List;
import java.util.Stack;

public interface IMyStack<T> {
    T pop() throws ADTException;
    void push (T v);

    boolean isEmpty();
    public Stack<T> getContent();
    List<T> getReversed();

}
