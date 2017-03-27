'use strict'

/**
 * Abstract Factory
 * ------------------
 * Design patterns that uses interfaces and abstract classes to 
 * ensure that each concrete class can be accessed through a factory method
 * so you can get a different object, without knowing the specifics of which object you need
 * hiding the class construction from the user.
 */

// Interfaces
class ShapeInterface {
    draw() {
        throw new Error('not implimented exception');
    }
}

class ColorInterface {
    fill() {
        throw new Error('not implimented exception');
    }
}

// Abstract Classes
class AbstractFactory {
    getColor(color) {}
    getShape(shapeType) {}
}

// Factory Classes
class ShapeFactory extends AbstractFactory {

    getShape(shapeType) {
        if( shapeType === null )
            return null;

        switch(shapeType.toLowerCase()){
            case 'circle':
                return new Circle();

            case 'rectangle':
                return new Rectangle();

            case 'square':
                return new Square();
            
            default:
                return null;
        }
    }

    getColor(color) {
        return null;
    }
}

class ColorFactory extends AbstractFactory {

    getShape(shapeType) {
        return null;
    }

    getColor(color){
        if( color === null )
            return null;

        switch(color.toLowerCase()){
            case 'red':
                return new Red();

            case 'green':
                return new Green();

            case 'blue':
                return new Blue();
            
            default:
                return null;
        }
    }

}

// Factory Producer
class FactoryProducer {
    static getFactory(choice) {

        switch(choice.toLowerCase()) {
            case 'shape':
                return new ShapeFactory();
            case 'color':
                return new ColorFactory();
            default:
                return null;
        }

    }
}

// Concrete classes

// Shapes
class Rectangle extends ShapeInterface {
    draw() {
        console.log("Inside Rectangle.draw() method.");
    }
}

class Circle extends ShapeInterface {
    draw() {
        console.log("Inside Circle.draw() method.");
    }
}

class Square extends ShapeInterface {
    draw() {
        console.log("Inside Square.draw() method.");
    }
}

// Colors
class Red extends ColorInterface {
    fill() {
        console.log("Inside Red.fill() method.");
    }
}

class Green extends ColorInterface {
    fill() {
        console.log("Inside Green.fill() method.");
    }
}

class Blue extends ColorInterface {
    fill() {
        console.log("Inside Blue.fill() method.");
    }
}

// Test Code
var shapeFactory = FactoryProducer.getFactory('shape');

var shape1 = shapeFactory.getShape('Circle');
shape1.draw();