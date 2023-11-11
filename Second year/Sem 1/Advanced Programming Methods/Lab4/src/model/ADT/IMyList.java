package model.ADT;

import model.exception.ADTException;
import model.exception.MyException;

public interface IMyList<T> {
    void add(T item);
    void remove(T item) throws ADTException;

}
