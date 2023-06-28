import Head from 'next/head';
import Header from './common/Header';
import SiteFooter from './common/Footer';

export default function Layout({ children }) {
    return (
      <>
        {/* <Head>
          <title>Real Estate</title>
        </Head> */}
        <header>
          <Header />
        </header>
        <main className="container mx-auto md:my-4">
          {children}
        </main>
        <footer>
          <SiteFooter />
        </footer>
      </>
    );
  }