from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential

def main():
    # setup training and test data
    training_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    training_set = training_datagen.flow_from_directory('Dataset/Train', target_size=(225, 225), batch_size=32, class_mode='categorical')
    test_set = test_datagen.flow_from_directory('Dataset/Test', target_size=(225, 225), batch_size=32, class_mode='categorical')

    # declare architecture
    model = Sequential()

    print('-----------------------------------------------------------------')

    model.add(Conv2D(16, (3, 3), input_shape=(225, 225, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(328, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(500, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # build and train
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(training_set, validation_data=test_set, epochs=15, steps_per_epoch=len(training_set), validation_steps=len(test_set))

    print('-----------------------------------------------------------------')
    
    model.summary()
    model.save('model.h5')

if __name__ == "__main__":
    main()