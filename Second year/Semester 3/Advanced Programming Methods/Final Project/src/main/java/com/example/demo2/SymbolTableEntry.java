package com.example.demo2;

import javafx.beans.property.SimpleStringProperty;
import model.value.Value;

public class SymbolTableEntry
{
    private SimpleStringProperty variableName;
    private SimpleStringProperty value;


    public SymbolTableEntry(String variableName, Value value){
        this.variableName = new SimpleStringProperty(variableName);
        this.value = new SimpleStringProperty(value.toString());
    }

    public SimpleStringProperty variableNameProperty(){
        return this.variableName;
    }

    public SimpleStringProperty valueProperty(){
        return this.value;
    }

    public String getVariableName(){
        return this.variableName.get();
    }

    public String getValue(){
        return this.value.get();
    }

    public void setVariableName(String newVariableName){
        this.variableName.set(newVariableName);
    }

    public void setValue(String newValue){
        this.value.set(newValue);
    }

}