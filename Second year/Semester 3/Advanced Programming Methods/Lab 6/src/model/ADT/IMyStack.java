package model.ADT;

import model.exception.ADTException;
public interface IMyStack<T> {
    T pop() throws ADTException;
    void push (T v);

    boolean isEmpty();
}
