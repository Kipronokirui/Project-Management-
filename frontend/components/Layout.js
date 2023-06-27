import Head from 'next/head';
import Header from './common/Header';
import Footer from './common/Footer';

export default function Layout({ children }) {
    return (
      <>
        <Head>
          <title>Real Estate</title>
        </Head>
        <header>
          <Header />
        </header>
        <main>{children}</main>
        <footer>
          <Footer />
        </footer>
      </>
    );
  }