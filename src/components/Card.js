import React from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet } from 'react-native';

const ProductCard = ({ product, onPress }) => {
    return (
        <TouchableOpacity onPress={() => onPress(product)} style={styles.card}>
            <View style={styles.imageContainer}>
                <Image
                    source={{ uri: product.mainImage }}
                    style={styles.image}
                    resizeMode="cover"
                />
            </View>
            <View style={styles.infoContainer}>
                <Text style={styles.title} numberOfLines={1}>
                    {product.title}
                </Text>
                <Text style={styles.price}>${product.price.toFixed(2)}</Text>
                <Text style={styles.description} numberOfLines={2}>
                    {product.shortDescription}
                </Text>
            </View>
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    card: {
        backgroundColor: '#fff',
        borderRadius: 10,
        overflow: 'hidden',
        margin: 10,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 4,
        elevation: 3,
        width: 250,
        height: 330,
    },
    imageContainer: {
        width: '100%',
        aspectRatio: 4 / 3,
    },
    image: {
        width: '100%',
        height: '100%',
    },
    infoContainer: {
        padding: 15,
        flex: 1,
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 5,
    },
    price: {
        fontSize: 16,
        color: '#2ecc71',
        fontWeight: 'bold',
        marginBottom: 8,
    },
    description: {
        fontSize: 14,
        color: '#666',
    },
});

export default ProductCard;
