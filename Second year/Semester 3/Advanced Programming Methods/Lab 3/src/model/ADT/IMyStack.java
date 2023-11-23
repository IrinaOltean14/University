package model.ADT;
import model.exception.*;
public interface IMyStack<T> {
    T pop() throws ADTException;
    void push (T v);

    boolean isEmpty();
}
