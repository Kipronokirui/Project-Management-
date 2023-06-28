import React from 'react'
import Head from 'next/head';
import Posts from '../../components/posts/Posts';

export default function CategoryDetails ({ data }) {
    return (
        <>
            <Head>
                <title>{data.title}</title>
                <meta name="description" content={data.title} />
                <link rel="icon" href="/logo.ico" />
            </Head>
            <div>{data.title}</div>
            <div className="grid grid-cols-4 gap-4">
                {data.posts.map((post) => (
                    <Posts key={post.post_id} post={post} />
                ))}
                
            </div>
        </>
  )
}

export async function getStaticPaths() {
    const response = await fetch('http://127.0.0.1:8000/categorys/')
    const data = await response.json();
    const allSlugs = data.map(item => item.slug)
    const paths = allSlugs.map(slug => ({ params: { slug: slug } }))
    
    return {
      paths,
      fallback:false,
    }
  }
export async function getStaticProps({params}) {
    const response = await fetch(`http://127.0.0.1:8000/category/${params.slug}`);
    const data = await response.json();
  
    return {
      props: {
        data,
      },
    }
  }