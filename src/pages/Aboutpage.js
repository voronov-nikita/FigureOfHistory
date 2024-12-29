import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export const AboutScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styleText.title}>Пример заголовка</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

const styleText = StyleSheet.create({
  title: {
    fontSize: "10%"
  },

  main: {

  },

  important: {

  }
})
