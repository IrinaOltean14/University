package model.ADT;

import model.exception.ADTException;

public interface IMyList<T> {
    void add(T item);
    void remove(T item) throws ADTException;

}
