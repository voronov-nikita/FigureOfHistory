import { View, FlatList, StyleSheet, useWindowDimensions } from 'react-native';
import ProductCard from './Card';

const ProductsList = ({ products, onProductPress }) => {
    const { width } = useWindowDimensions();

    // Определяем количество колонок в зависимости от ширины экрана
    const numColumns = width > 600 ? Math.floor(width / 270) : 2;

    return (
        <View style={styles.container}>
            <FlatList
                data={products}
                keyExtractor={item => item.id.toString()}
                renderItem={({ item }) => (
                    <ProductCard product={item} onPress={onProductPress} />
                )}
                numColumns={numColumns}
                contentContainerStyle={styles.listContent}
                key={numColumns} // Пересоздаем список при изменении количества колонок
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 5,
    },
    listContent: {
        alignItems: 'center',
    },
});

export default ProductsList;
