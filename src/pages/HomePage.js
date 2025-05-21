import {
    View,
    ScrollView,
    Image,
    Text,
    StyleSheet,
    Dimensions,
} from 'react-native';

const ProductDetailScreen = ({ route }) => {
    const { product } = route.params;
    const { width } = Dimensions.get('window');

    return (
        <ScrollView style={styles.container}>
            <View style={styles.imageGallery}>
                <Image
                    source={{ uri: product.mainImage }}
                    style={[
                        styles.mainImage,
                        { width: width - 40, height: (width - 40) * 0.75 },
                    ]}
                />
                <View style={styles.additionalImages}>
                    {product.additionalImages.map((image, index) => (
                        <Image
                            key={index}
                            source={{ uri: image }}
                            style={[
                                styles.additionalImage,
                                {
                                    width: (width - 60) / 3,
                                    height: (width - 60) / 3,
                                },
                            ]}
                        />
                    ))}
                </View>
            </View>

            <View style={styles.details}>
                <Text style={styles.title}>{product.title}</Text>
                <Text style={styles.price}>${product.price.toFixed(2)}</Text>
                <Text style={styles.description}>
                    {product.longDescription}
                </Text>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        padding: 20,
    },
    imageGallery: {
        marginBottom: 20,
    },
    mainImage: {
        borderRadius: 10,
        marginBottom: 10,
    },
    additionalImages: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
    },
    additionalImage: {
        borderRadius: 5,
        marginBottom: 10,
    },
    details: {
        paddingHorizontal: 5,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    price: {
        fontSize: 22,
        color: '#2ecc71',
        fontWeight: 'bold',
        marginBottom: 20,
    },
    description: {
        fontSize: 16,
        lineHeight: 24,
        color: '#333',
    },
});

export default ProductDetailScreen;
